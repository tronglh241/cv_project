import abc
import inspect
import os
from pathlib import Path
from typing import Any, Union


class Project(abc.ABC):
    def __init__(self, config_path: Union[str, os.PathLike] = None):
        super(Project, self).__init__()

        if config_path is None:
            self.config_path = Path(inspect.getfile(self.__class__)).with_name('config.yaml')
        else:
            self.config_path = Path(config_path)

        if not self.config_path.exists():
            raise FileNotFoundError(f'{config_path} not found.')

    @abc.abstractmethod
    def run(self, *args: Any) -> Any:
        pass

    def __call__(self, *args: Any) -> Any:
        output = self.run(*args)
        return output
