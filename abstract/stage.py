import utils
import inspect

from abstract.processor import Processor
from abstract.adapter import InAdapter, OutAdapter


class Stage:
    def __init__(self, mode=None, config_path=None, in_adapter_mode=None, out_adapter_mode=None,
                 adapter_config_path=None, *args, **kwargs):
        self.processor = self._create_processor(mode, config_path, Processor, 'config.yaml', *args, **kwargs)
        self.in_adapter = self._create_processor(in_adapter_mode, adapter_config_path, InAdapter, 'adapter.yaml')
        self.out_adapter = self._create_processor(out_adapter_mode, adapter_config_path, OutAdapter, 'adapter.yaml')

    def preprocess(self, *args):
        return args

    def postprocess(self, *args):
        return args

    def __call__(self, *args):
        output = self.in_adapter(args)
        output = self.preprocess(*output)
        output = self.processor(*output)
        output = self.postprocess(*output)
        output = self.out_adapter(args, output)
        return output

    def _create_processor(self, mode=None, config_path=None, default_processor_cls=None,
                          default_config_filename='config.yaml', *args, **kwargs):
        if config_path is None:
            config_path = utils.Path(inspect.getfile(self.__class__)).with_name(default_config_filename)

        if mode is None:
            processor = default_processor_cls()
        elif config_path.exists():
            config = utils.load_yaml(config_path)
            processor = utils.eval_config(config[mode], *args, **kwargs)
        else:
            raise FileNotFoundError('{} not found.'.format(config_path))

        return processor
