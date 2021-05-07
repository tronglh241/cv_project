import inspect
from pathlib import Path
from typing import Any, Tuple, Type, Union

import utils
from abstract.adapter import InAdapter, OutAdapter
from abstract.processor import Processor


class Stage:
    def __init__(self, mode: str = None, config_path: str = None,
                 in_adapter_mode: str = None, out_adapter_mode: str = None,
                 adapter_config_path: str = None):
        self.processor = self._create_processor(mode, config_path,
                                                default_processor_cls=Processor,
                                                default_config_filename='config.yaml')
        self.in_adapter = self._create_processor(in_adapter_mode, adapter_config_path,
                                                 default_processor_cls=InAdapter,
                                                 default_config_filename='adapter.yaml')
        self.out_adapter = self._create_processor(out_adapter_mode, adapter_config_path,
                                                  default_processor_cls=OutAdapter,
                                                  default_config_filename='adapter.yaml')

    def preprocess(self, *args: Any) -> Tuple:
        return args

    def postprocess(self, *args: Any) -> Tuple:
        return args

    def __call__(self, *args: Any) -> Tuple:
        output = self.in_adapter(args)
        output = self.preprocess(*output)
        output = self.processor(*output)
        output = self.postprocess(*output)
        output = self.out_adapter(args, output)
        return output

    def _create_processor(self, mode: str = None, config_path: Union[str, Path] = None, *,
                          default_processor_cls: Type[Any], default_config_filename: str = 'config.yaml') -> Any:
        if config_path is None:
            config_path = Path(inspect.getfile(self.__class__)).with_name(default_config_filename)
        elif isinstance(config_path, str):
            config_path = Path(config_path)

        if mode is None:
            processor = default_processor_cls()
        elif config_path.exists():
            config = utils.load_yaml(config_path)
            processor = utils.eval_config(config[mode])
        else:
            raise FileNotFoundError(f'{config_path} not found.')

        return processor
