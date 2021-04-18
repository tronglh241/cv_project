class DTO:
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
            raise ValueError('Unsupported type {}.'.format(type(obj)))

    def asdict(self):
        return {key: DTO._asdict(value) for key, value in self.__dict__.items() if value is not None}

    def __repr__(self):
        _repr = '{}('.format(self.__class__.__name__)
        for key, value in self.__dict__.items():
            _repr += '{}={!r}, '.format(key, value)
        _repr = '{})'.format(_repr[:-2])

        return _repr
