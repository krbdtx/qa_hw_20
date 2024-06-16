import os

from appium.options.android import UiAutomator2Options
from pydantic import BaseModel
from utils.file import abs_path_from_project


class Config(BaseModel):
    context: str
    remote_url: str = os.getenv('REMOTE_URL')
    device_name: str = os.getenv('DEVICE_NAME')
    app_name: str = os.getenv('APP_NAME')
    app_wait_activity: str = os.getenv('APP_WAIT_ACTIVITY')
    app_local_path: str = abs_path_from_project(os.getenv('APP'))
    app_bstack_path: str = os.getenv('APP')
    platform_name: str = os.getenv('PLATFORM_NAME')
    platform_version: str = os.getenv('PLATFORM_VERSION')
    udid: str = os.getenv('UDID')
    user_name: str = os.getenv('USER_NAME')
    access_key: str = os.getenv('ACCESS_KEY')
    def to_driver_options(self, context):
        options = UiAutomator2Options()

        if context in ['local_emulator', 'local_real']:
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('appWaitActivity', self.app_wait_activity)
            options.set_capability('app', self.app_local_path)
            options.set_capability('udid', self.udid)

        if context == 'bstack':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('deviceName', self.device_name)
            options.set_capability('platformName', self.platform_name)
            options.set_capability('platformVersion', self.platform_version)
            options.set_capability('appWaitActivity', self.app_wait_activity)
            options.set_capability('app', self.app_bstack_path)
            options.set_capability(
                'bstack:options', {
                    'projectName': 'Wikipedia',
                    'buildName': 'Wikipedia',
                    'sessionName': 'Wikipedia',
                    'userName': self.user_name,
                    'accessKey': self.access_key,
                },
            )

        return options


config = Config(context='local_emulator')
