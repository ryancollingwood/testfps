from ursina.entity import Entity
from ursina.sequence import Sequence, Func, Wait
from ursina import color

DEFAULT_TEXTURE = "white_cube"
DEFAULT_COLLIDER = "box"
DEFAULT_COLOR = color.white
DEFAULT_MODEL = "cube"


class Thing(Entity):

    def __init__(
            self,
            parent,
            x,
            z,
            y = None,
            rotation = 0,
            model = DEFAULT_MODEL,
            scale = (1, 1, 1,),
            color = DEFAULT_COLOR,
            collider = DEFAULT_COLLIDER,
            texture = DEFAULT_TEXTURE,
            add_to_scene_entities = True,
            **kwargs
    ):
        place_y = y
        if place_y is None:
            place_y = scale[1] / 2

        super(Thing, self).__init__(
            parent = parent,
            x = x,
            y = place_y,
            z = z,
            rotation = rotation,
            model = model,
            scale = scale,
            color = color,
            collider = collider,
            texture = texture,
            add_to_scene_entities = add_to_scene_entities,
            **kwargs
        )

        self.update_ticks = 0
        self.update_ticks_interval = 30

        self.position = (x, y, z)
        self.orginal_x = x
        self.orignal_y = y
        self.orignal_z = z

        for key, value in kwargs.items():
            setattr(self, key, value)

    def update(self):

        if self.update_ticks < self.update_ticks_interval:
            self.update_ticks += 1
            return False

        self.update_ticks = 0
        return True

    def collide(self, other):
        pass

    def push(self, who = None):
        pass

    def que(self, delay, func, **kwargs):
        s = Sequence(
            Wait(delay),
            Func(func, **kwargs)
        )
        s.start()
