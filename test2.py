from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.raycaster import raycast
from geom import build_cube_wall, build_wall, build_flat_wall, grid_place, item_place
from geom import CUBE_SIZE, HALF_CUBE_SIZE
import npcs
from things import Thing




if __name__ == '__main__':
    app = Ursina()
    world = Entity()
    Sky(color=color.gray)
    Entity(model='plane', scale=100, color=color.yellow.tint(-.2), texture='white_cube', texture_scale=(100,100), collider='box')
    player = FirstPersonController(y=2, origin_y=-.5)
    player.gun = None

    t = Thing(world, 0, 0)

    tiles = dict()
    for tile in ["brick_red", "fence_stone", "platformIndustrial_095", "platformIndustrial_106"]:
        tiles[tile] = load_texture(tile, "resources/tiles/")

    sprites = dict()
    for sprite in ["mguard_s_1"]:
        sprites[sprite] = load_texture(sprite, "resources/npcs/guard/")

    level_blocks = list()
    level_def = [
        "                 ",
        "                 ",
        "                 ",
        "        @        ",
        "                 ",
        "                 ",
        "                 ",
    ]

    for z, row in enumerate(level_def):
        for x, col in enumerate(row):
            if col == "#":
                level_blocks.append(
                    build_cube_wall(world, x, z, tiles["brick_red"])
                )
            elif col == "|":
                level_blocks.append(
                    build_flat_wall(world, x, z,
                                    tiles["platformIndustrial_095"],
                                    False,
                                    ))
            elif col == "-":
                door = build_flat_wall(
                    world, x, z,
                    tiles["platformIndustrial_095"],
                    True
                )
                level_blocks.append(door)
            elif col == "@":
                player.position = item_place(x, z)
            elif col == "!":
                npc_place = item_place(x, z)

                baddie = npcs.Npc(
                    texture = sprites['mguard_s_1'],
                    parent = world,
                    x = npc_place[0],
                    y = (CUBE_SIZE / 2),
                    z = npc_place[2],
                    rotation = Vec3(0,0,0),
                    scale = (CUBE_SIZE, CUBE_SIZE -0.1, 0.1),
                )

    app.run()

