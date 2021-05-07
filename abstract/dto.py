import abc


class DTO(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        pass

    @staticmethod
    def _asdict(obj):
        if isinstance(obj, dict):
            return {key: DTO._asdict(value) for key, value in obj.items() if value is not None}
        elif isinstance(obj, list):
            return [DTO._asdict(element) for element in obj if element is not None]
        elif isinstance(obj, tuple):
            return tuple([DTO._asdict(element) for element in obj if element is not None])
        elif isinstance(obj, (int, float, str, bool)):
            return obj
        elif isinstance(obj, DTO):
            return obj.asdict()
        else:
            raise ValueError(f'Unsupported type {type(obj)} in object {obj}.')

    def asdict(self):
        return {key: DTO._asdict(value) for key, value in self.__dict__.items() if value is not None}

    def __repr__(self):
        _repr = f'{self.__class__.__name__}('

        for key, value in self.__dict__.items():
            _repr += f'{key}={value!r}, '

        _repr = f'{_repr[:-2]})'

        return _repr
