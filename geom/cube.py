from panda3d.core import Vec3

from .wall import Wall


class Cube(Wall):
    def __init__(
            self,
            parent,
            x,
            z,
            height,
            width,
            depth,
            texture,
            rotation = Vec3(0, 0, 0),
            stretch_texture = False,
            **kwargs,
    ):

        super(Cube, self).__init__(
            parent = parent,
            x = x,
            z = z,
            height = height,
            width = width,
            depth = depth,
            rotation = rotation,
            texture = texture,
            stretch_texture = stretch_texture,
            model="cube",
            auto_shade=True,
            #**kwargs,
        )
