from ursina.vec3 import Vec3
from .cube import Cube
from .wall import Wall
from .flatwall import FlatWall


CUBE_SIZE = 4
HALF_CUBE_SIZE = CUBE_SIZE / 2
DEFAULT_TEXTURE = "white_cube"


def build_wall(
        parent, x, z,
        height, width = 1, depth = 1,
        rotation = Vec3(0, 0, 0),
        texture = "brick_red",
        stretch_texture = False,
        model = "cube",
        **kwargs,
):
    if texture is None:
        texture = DEFAULT_TEXTURE

    e = Wall(
        parent = parent,
        model = model,
        height = height, width = width, depth = depth,
        x = x + width / 2,
        z = z + depth / 2,
        texture = texture,
        rotation = rotation,
        auto_shade = True,
        **kwargs,
    )

    if not stretch_texture:
        e.texture_scale = (e.scale_z, e.scale_y)
    else:
        e.texture_scale = (1, 1)

    return e


def build_cube_wall(
        parent, x, z, texture, rotation = Vec3(0,0,0),
        stretch_texture = False, **kwargs
):

    cube_wall_position = grid_place(x, z)

    return Cube(
        parent,
        cube_wall_position[0],
        cube_wall_position[1],
        CUBE_SIZE, CUBE_SIZE, CUBE_SIZE,
        texture, rotation, stretch_texture, **kwargs

    )


def build_flat_wall(
        parent, x, z, texture,
        horizontal,
        pushable = True,
        stretch_texture = True,
):
    cube_wall_postion = grid_place(x, z)

    return FlatWall(
        parent,
        cube_wall_postion[0],
        cube_wall_postion[1],
        CUBE_SIZE,
        CUBE_SIZE,
        CUBE_SIZE,
        texture,
        horizontal,
        pushable,
        stretch_texture = stretch_texture
    )


def grid_place(x, z):
    return (
        (x + 1) * CUBE_SIZE,
        (z + 1) * CUBE_SIZE,
    )


def item_place(x, z):
    return (
        ((x + 1) * CUBE_SIZE) + HALF_CUBE_SIZE,
        1,
        ((z + 1) * CUBE_SIZE) + HALF_CUBE_SIZE,
    )


