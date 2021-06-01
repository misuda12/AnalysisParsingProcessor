import os
import platform
import sys

import toml

CONFIG_VERSION = '0.1'

default = """
[window]
width = 300
height = 220
font-size = '10px'
opacity = 1.0
frameless = false
always_on_top = false

[app]

[config]
# do not change
version = '%s'
""" % CONFIG_VERSION

_script_path = sys.argv[0]
_config = None


def get_config_path():
    cfg_file_name = 'config.cfg'
    script_dir = os.path.dirname(_script_path)
    if platform.system() == 'Windows':
        return os.path.join(os.getenv('APPDATA', script_dir), cfg_file_name)
    else:
        return os.path.join(script_dir, cfg_file_name)


def config():
    global _config
    if _config:
        return _config

    config_file_path = get_config_path()

    try:
        with open(config_file_path, 'r') as config_file:
            config = toml.load(config_file)
            if config['config']['version'] != CONFIG_VERSION:
                raise Exception(f'Config version has changed from {config["config"]["version"]} to {CONFIG_VERSION}')
            _config = config
    except Exception as _:
        with open(config_file_path, 'w') as config_file:
            config_file.write(default)
            _config = toml.load(default)
    return _config