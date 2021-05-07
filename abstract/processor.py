from typing import Any, Tuple


class Processor:
    def preprocess(self, *args: Any) -> Tuple:
        return args

    def process(self, *args: Any) -> Tuple:
        return args

    def postprocess(self, *args: Any) -> Tuple:
        return args

    def __call__(self, *args: Any) -> Tuple:
        output = self.preprocess(*args)
        output = self.process(*output)
        output = self.postprocess(*output)
        return output
