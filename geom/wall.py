import random

from ursina import color
from panda3d.core import Vec3

from things import Thing


class Wall(Thing):
    def __init__(
            self,
            parent, x, z,
            height, width=1, depth=1,
            rotation=Vec3(0, 0, 0),
            texture="brick_red",
            stretch_texture=False,
            model="cube",
            auto_shade=True,
            **kwargs
    ):

        y = height / 2

        if auto_shade:
            wall_colour = color.color(0, 0, random.uniform(.9, 1.0))
        else:
            wall_colour = None

        if texture is None:
            texture = "white_cube"

        self.horizontal = False

        super(Wall, self).__init__(
            parent = parent,
            model = model,
            scale = (width, height, depth),
            x = x + width / 2,
            y = y,
            z = z + depth / 2,
            collider = 'box',
            texture = texture,
            color = wall_colour,
            rotation = rotation,
            **kwargs,
        )

        self.pushable = False
        self.pushing = False
        self.push_duration = 1.8

        if not stretch_texture:
            self.texture_scale = (self.scale_z, self.scale_y)
        else:
            self.texture_scale = (1, 1)

    def reset_pushing(self):
        self.pushing = not self.pushing

    def set_horizontal(self, horizontal):
        self.horizontal = horizontal

    def set_pushable(self, pushable):
        self.pushable = pushable

    def push(self, who = None):
        if self.pushable and not self.pushing:
            self.pushing = True
            duration = self.push_duration

            if self.horizontal:
                self.animate_position((self.x + self.scale_x, self.y, self.z), duration=duration)
            else:
                self.animate_position((self.x, self.y, self.z + self.scale_z), duration=duration)

            self.animate_position((self.x, self.y, self.z), duration=duration, delay=duration)
            self.que(duration*2, self.reset_pushing)
