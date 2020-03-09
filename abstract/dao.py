class DAO(object):
    def asdict(self):
        def _asdict(obj):
            if isinstance(obj, dict):
                return {key: _asdict(value) for key, value in obj.items()}
            elif isinstance(obj, list):
                return [_asdict(element) for element in obj]
            elif isinstance(obj, tuple):
                return tuple([_asdict(element) for element in obj])
            elif isinstance(obj, (int, float, str, bool)):
                return obj
            elif isinstance(obj, DAO):
                return obj.asdict()
            else:
                raise ValueError('Unsupported type {}.'.format(type(obj)))

        return {key: _asdict(value) for key, value in self.__dict__.items()}

    def __repr__(self):
        _repr = '{}('.format(self.__class__.__name__)
        for key, value in self.__dict__.items():
            _repr += '{}={!r}, '.format(key, value)
        _repr = '{})'.format(_repr[:-2])
        
        return _repr