import os

assets_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), '..', 'assets')

script_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), '..', 'script')


def assets(file):
    return os.path.join(assets_path, file)


def script(file):
    return os.path.join(script_path, file)
