from ursina.entity import Entity
from ursina.sequence import Sequence, Func, Wait

class Thing(Entity):

    def __init__(
            self,
            parent,
            model,
            scale,
            x,
            y,
            z,
            collider,
            texture,
            color,
            rotation,
            add_to_scene_entities=True,
            **kwargs
    ):
        super(Thing, self).__init__(
            parent = parent,
            model = model,
            scale = scale,
            x = x,
            y = y,
            z = z,
            collider = collider,
            texture = texture,
            color = color,
            rotation = rotation,
            add_to_scene_entities = add_to_scene_entities,
            **kwargs
        )

        self.orginal_x = x
        self.orignal_y = y
        self.orignal_z = z

    def que(self, delay, func, **kwargs):
        s = Sequence(
            Wait(delay),
            Func(func, **kwargs)
        )
        s.start()