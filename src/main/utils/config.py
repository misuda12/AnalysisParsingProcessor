import os
import platform
import sys
import toml

CONFIG_VERSION = '1.0'

default = """
[window]
width = 1280
height = 720
font-size = '10px'
opacity = 1.0
frameless = false
always_on_top = false

[application]

[config]
# DO NOT CHANGE
version = '%s'
""" % CONFIG_VERSION

_script_path = sys.argv[0]
_config = None


def get_config_path():
    config_file_name = 'config.cfg'
    script_directory = os.path.dirname(_script_path)
    if platform.system() == 'Windows':
        return os.path.join(os.getenv('APPDATA', script_directory), config_file_name)
    else:
        return os.path.join(script_directory, config_file_name)


def config():
    global _config
    if _config:
        return _config
    config_file = get_config_path()
    try:
        with open(config_file, "r") as cfg_file:
            cfg = toml.load(cfg_file)
            if cfg['config']['version'] != CONFIG_VERSION:
                raise Exception('Version has changed')
            _config = cfg
    except Exception as _:
        with open(config_file, "w") as cfg_file:
            cfg_file.write(default)
            _config = toml.loads(default)
    return _config