from ursina import Ursina, Sky, Entity, load_texture, color
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import scene
from ursina.raycaster import raycast
import npcs
from things import Thing
from game import World




if __name__ == '__main__':
    app = Ursina()

    tiles = dict()
    for tile in ["brick_red", "fence_stone", "platformIndustrial_095", "platformIndustrial_106"]:
        tiles[tile] = load_texture(tile, "resources/tiles/")

    sprites = dict()
    for sprite in ["mguard_s_1"]:
        sprites[sprite] = load_texture(sprite, "resources/npcs/guard/")

    player = FirstPersonController(y=2, origin_y=-.5)
    player.gun = None

    world = World(player, tiles, sprites, parent = scene)    

    level_def = [
        "##### ###",
        "#..@....#",
        "#########",
    ]

    world.build(level_def)

    #Sky(color=color.gray)
    #floor = Entity(model='plane', scale=100, color=color.yellow.tint(-.2), texture='white_cube', texture_scale=(100,100), collider='box')

    t = Thing(world, 0, 0)


    app.run()

