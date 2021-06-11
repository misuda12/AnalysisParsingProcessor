import os

assets_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), '..', 'assets')

script_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)),  '..', 'script')


def assets(name):
    return os.path.join(assets_path, name)


def script(name):
    return os.path.join(script_path, name)