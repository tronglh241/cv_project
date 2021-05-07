import abc
from typing import Tuple


class Adapter(abc.ABC):
    @abc.abstractmethod
    def convert(self, *args: Tuple) -> Tuple:
        pass

    def __call__(self, *args: Tuple) -> Tuple:
        output = self.convert(*args)
        return output


class InAdapter(Adapter):
    def convert(self, stage_input: Tuple) -> Tuple:
        return stage_input


class OutAdapter(Adapter):
    def convert(self, stage_input: Tuple, stage_output: Tuple) -> Tuple:
        return stage_output
