from pathlib import Path


def abs_path(path):
    if Path(path).is_absolute():
        return path
    else:
        return str(Path(__file__).parents[1].joinpath(path))
