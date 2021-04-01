import os
import sys
import pytest

from pathlib import Path

sys.path.append(os.environ['PWD'])

from project import Project  # noqa: E402


def image_paths():
    image_dir = 'test/test_full/data'
    image_pattern = '*.jpg'

    image_paths = [str(image_path) for image_path in Path(image_dir).glob(image_pattern)]
    return image_paths


@pytest.fixture
def detector():
    return Project()


@pytest.mark.parametrize('image_path', image_paths())
def test_full(detector, image_path):
    info = detector(image_path)
    pred = str(info['number'])
    target = Path(image_path).stem

    assert pred == target
