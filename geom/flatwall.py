from .wall import Wall


class FlatWall(Wall):

    def __init__(
            self,
            parent,
            x,
            z,
            height,
            width,
            depth,
            texture,
            horizontal,
            pushable,
            stretch_texture=True,
    ):
        rotation = (0, 90, 0)
        if horizontal:
            rotation = (0, 0, 0)

        super(FlatWall, self).__init__(
            parent,
            x,
            z,
            height,
            width,
            depth,
            texture = texture,
            rotation = rotation,
            stretch_texture = stretch_texture,
            model = "quad",
            double_sided = True,
            auto_shade = False
        )

        self.set_horizontal(horizontal)
        self.pushable = pushable
