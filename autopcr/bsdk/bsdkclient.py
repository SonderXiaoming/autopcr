
from .bsgamesdk import login
from .validator import autoValidator, manualValidator

async def _defaultLogger(msg):
    print(msg)

class bsdkclient:
    '''
        acccountinfo = {
            'account': '',
            'password': '',
            'platform': 2, # indicates android platform
            'channel': 1, # indicates bilibili channel
        }
    '''

    def __init__(self, acccountinfo, captchaVerifier=autoValidator, errlogger=_defaultLogger):
    # def __init__(self, acccountinfo, captchaVerifier=manualValidator, errlogger=_defaultLogger):
        self.account = acccountinfo['account']
        self.pwd = acccountinfo['password']
        self.platform = acccountinfo['platform']
        self.channel = acccountinfo['channel']
        self.captchaVerifier = captchaVerifier
        self.errlogger = errlogger

    async def login(self):
        while True:
            resp = await login(self.account, self.pwd, self.captchaVerifier)
            if resp['code'] == 0:
                await self.errlogger("geetest or captcha succeed")
                break
            await self.errlogger(resp['message'])
            raise ValueError(resp['message'])

        return resp['uid'], resp['access_key']
