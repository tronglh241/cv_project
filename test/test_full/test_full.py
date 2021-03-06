import os
import sys
sys.path.append(os.environ['PWD'])

from pathlib import Path
from project import Project

if __name__ == '__main__':
    image_dir = Path(sys.argv[1])
    image_pattern = sys.argv[2]

    detector = Project()

    for image_path in image_dir.glob(image_pattern):
        print(detector(str(image_path)))
