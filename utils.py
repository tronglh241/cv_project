import yaml

from pathlib import Path
from importlib import import_module


def load_yaml(yaml_file):
    with open(yaml_file) as f:
        configs = yaml.safe_load(f)
    return configs

def create_instance(config, *args, **kwargs):
    module = config['module']
    name = config['name']
    config_kwargs = config.get(name, {})
    for key, value in config_kwargs.items():
        if isinstance(value, str):
            config_kwargs[key] = eval(value)
    return getattr(import_module(module), name)(*args, **config_kwargs, **kwargs)

def abs_path(path):
    return str(Path(__file__).parent.joinpath(path))