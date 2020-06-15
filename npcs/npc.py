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
        #self.texture = self.sprites[texture_name]
        self.sprite.texture = self.sprites[texture_name]

    def push(self, who = None):
        return





