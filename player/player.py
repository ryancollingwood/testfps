from ursina.entity import Entity
from things import Thing

class Player(Things):

    def __init__(self, **kwargs):
        super(Thing, self).__init__(
            **kwargs
        )
        
        self.speed = 5
        self.update_interval = 30
        self.position = (0, 1, 1)

    def use(self):
        origin = self.world_position + self.up + (self.direction / 2)
        touch_ray = raycast(origin, self.forward, ignore = [self, ], distance = self.interact_distance, debug = False)

        if touch_ray.hit:
            touch_ray.entity.push(self)

    def update(self):
        if not Thing.update(self):
            return False
        
