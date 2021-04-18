import abc


class Adapter(abc.ABC):
    @abc.abstractmethod
    def convert(self, *args):
        pass

    def __call__(self, *args):
        output = self.convert(*args)
        return output


class InAdapter(Adapter):
    def convert(self, stage_input):
        return stage_input


class OutAdapter(Adapter):
    def convert(self, stage_input, stage_output):
        return stage_output
