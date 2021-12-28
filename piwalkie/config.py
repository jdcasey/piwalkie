import os
from ruamel.yaml import YAML


ETC_CONFIG_FILE = '/etc/piwalkie/config.yaml'
HOME_CONFIG_FILE = os.path.join(os.environ.get('HOME'), '.config/piwalkie/config.yaml')
TOKEN = 'token'
CHAT = 'chat'


# TODO: Make these configurable!!

WAV_THRESHOLD = 500


def load(config_file=None):
    config_path = config_file or HOME_CONFIG_FILE
    if os.path.exists(config_path) is not True:
        config_path = ETC_CONFIG_FILE

    if os.path.exists(config_path) is not True:
        raise Exception(f"No configuration defined for piwalkie in {config_file} or {HOME_CONFIG_FILE} or "
                        f"{ETC_CONFIG_FILE}")

    with open(config_path) as f:
        data = YAML().load(f)

    return Config(data)


class Config:
    def __init__(self, data):
        self.token = data.get(TOKEN)
        self.chat = data.get(CHAT)
