# 名字需要斟酌一下

from ..core.pcrclient import pcrclient
from .modulemgr import ModuleManager
import os, re
from typing import Dict, Iterator, List
from ..constants import CONFIG_PATH
from asyncio import Lock
import json
from .modulebase import Module
from copy import deepcopy

class AccountException(Exception):
    pass

class Account(ModuleManager):
    def __init__(self, parent: 'AccountManager', account: str, readonly: bool = False):
        if not account in parent.account_lock:
            parent.account_lock[account] = Lock()
        self._lck = parent.account_lock[account]
        self._account = account
        self._filename = parent.path(account)
        self.readonly = readonly

        with open(self._filename, 'r') as f:
            self.data = json.load(f)
            self.old_data = deepcopy(self.data)

        self.qq = self.data.get("qq", "")
        self.alian = self.data.get("alian", "未知")
        self.username = self.data.get("username", "")
        super().__init__(self.data.get("config", {}), self)
    
    async def __aenter__(self):
        if not self.readonly:
            await self._lck.acquire()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if not self.readonly:
            if self.data != self.old_data:
                await self.save_data()
            self._lck.release()

    async def save_data(self):
        with open(self._filename, 'w') as f:
            json.dump(self.data, f)

    async def set_result(self, result):
        self.data.setdefault('_last_result', {}).update(result)

    def get_client(self) -> pcrclient:
        return self.get_android_client()

    def get_ios_client(self) -> pcrclient: # Header TODO
        client = pcrclient({
            'account': self.data['username'],
            'password': self.data['password'],
            'channel': 1000,
            'platform': 1
        })
        return client

    def get_android_client(self) -> pcrclient:
        client = pcrclient({
            'account': self.data['username'],
            'password': self.data['password'],
            'channel': 1,
            'platform': 2
        })
        return client

    def generate_info(self):
        def _mask_str(mask_str: str) -> str:
            if not isinstance(mask_str, str):
                raise ValueError("Input must be a string")
            elif not mask_str:
                return ""
            else:
                return "*" * 7 + mask_str[-1]
            # elif len(mask_str) <= 1:
            #     return "*" * len(mask_str)
            # elif len(mask_str) == 2:
            #     return mask_str[0] + "*"
            # else:
            #     return mask_str[0] + "*" * (len(mask_str) - 2) + mask_str[-1]
        return {
            'alian': self.data['alian'],
            'qq': _mask_str(self.data['qq']),
            'username': _mask_str(self.data['username']),
            'password': 8 * "*",
        }

    def generate_daily_info(self):
        info = { 'last_result': self.data.get('_last_result', {}) }
        info.update(super().generate_daily_config())
        return info

    def generate_tools_info(self):
        info = { 'last_result': self.data.get('_last_result', {}) }
        info.update(super().generate_tools_config())
        return info

class AccountManager:
    pathsyntax = re.compile(r'[^\\\|?*/]{1,32}')

    def __init__(self, root: str):
        self.root = root
        self.account_lock: Dict[str, Lock] = {}

    def path(self, account: str) -> str:
        return os.path.join(self.root, account + '.json')

    def load(self, account: str, readonly: bool = False) -> Account:
        if not AccountManager.pathsyntax.fullmatch(account):
            raise AccountException('Invalid account name')
        return Account(self, account, readonly)

    def delete(self, account: str):
        if not AccountManager.pathsyntax.fullmatch(account):
            raise AccountException('Invalid account name')
        os.remove(self.path(account))
    
    def accounts(self) -> Iterator[str]:
        for fn in os.listdir(self.root):
            if fn.endswith('.json'):
                yield fn[:-5]


instance = AccountManager(os.path.join(CONFIG_PATH))
