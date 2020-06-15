from utils import convert_bmp_to_png
from pathlib import Path


if __name__ == "__main__":
    resource_path = Path("resources")
    for bmp_file in resource_path.glob('**/*.bmp'):
        print(bmp_file)
        convert_bmp_to_png(bmp_file, (152, 0, 136))


