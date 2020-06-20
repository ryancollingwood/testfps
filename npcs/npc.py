from things import Thing
from utils import load_textures
from ursina import Entity, Sprite, color
from math import atan, atan2, radians
from ursina import Vec3


class Npc(Thing):
    def __init__(self, parent, scale, x, y, z,
                 texture, rotation, **kwargs):

        super(Npc, self).__init__(
            parent,
            model = "quad",
            scale = scale,
            x = x,
            y = y,
            z = z,
            collider='box',
            texture = None,
            color = color.clear,            
            rotation = rotation,
            add_to_scene_entities=True,
            texture_scale = (1, 0.99),
            #double_sided = False,
            **kwargs
        )

        self.sprites = load_textures("resources/npcs/guard")
        self.base_name = "mguard"
        self.side = 1
        self.animation = "s"
        self.frame = None
        self.setBillboardAxis()

        # TODO maybe add a sprite to this?
        self.sprite = Sprite(
            model = "quad",
            parent = parent,
            scale = scale,
            x = x,
            y = y,
            z = z,
            texture = texture,
            texture_scale = (1, 0.99),
            double_sided = False,
            add_to_scene_entities=True,
            **kwargs,
        )
        self.sprite.setBillboardAxis()

    def get_sprite_name(self):
        return f"{self.base_name}_{self.animation}_{self.side}"

    def update_texture(self):
        texture_name = self.get_sprite_name()
        self.sprite.texture = self.sprites[texture_name]

    def push(self, who = None):
        return

    def update_facing(self, relative_to_rotation):
        relative_rotation = (relative_to_rotation - self.rotation)[1]

        while abs(relative_rotation) > 360:
            relative_rotation = relative_rotation % 360

        if relative_rotation < 0:
            relative_rotation = 360 + relative_rotation
  
        angle_sides = (
            (22.5, 67.5, 8),
            (67.5, 112.5, 7),
            (112.5, 157.5, 6),
            (157.5, 202.5, 5),
            (202.5, 247.5, 4),
            (247.5, 292.5, 3),
            (292.5, 337.5, 2),
            (0, 22.5, 1),
            (337.5, 361, 1),
            )
        
        match_side = [x for x in angle_sides if relative_rotation >= x[0] and relative_rotation < x[1]]                
        if len(match_side) == 0:
            raise Exception(f"Couldnt get a NPC sprite for relative_rotation: {relative_rotation}")

        if len(match_side) > 0:
            self.side = match_side[0][2]
            if self.side == 0:
                self.side = 1
            
            self.update_texture()






