from pathlib import Path
from ursina.texture_importer import load_texture


def load_textures(path):
    result = {}
    base_path = Path.cwd()
    for filename in base_path.glob(f'{path}/*.png'):
        result[filename.stem] = load_texture(filename.name, filename.parent)
    return result
