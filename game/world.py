from ursina import Sky, color
from ursina.entity import Entity
from geom import build_cube_wall, build_wall, build_flat_wall, grid_place, item_place
from geom import CUBE_SIZE, HALF_CUBE_SIZE


class World(Entity):

    def __init__(self, player: Entity, tiles, sprites, **kwargs):

        super(World, self).__init__(
            **kwargs
        )

        self.player = player
        self.sprites = sprites
        self.tiles = tiles

        self.level_blocks = None
    

    def build(self, level_def):
        self.level_blocks = list()

        Sky(color=color.gray, parent=self)

        len_rows = len(level_def)
        len_cols = 0

        for z, row in enumerate(level_def):
            
            if len(row) > len_cols:
                len_cols = len(row)

            for x, col in enumerate(row):
                if col == "#":
                    self.level_blocks.append(
                        build_cube_wall(self, x, z, self.tiles["brick_red"])
                    )

                elif col == "|":
                    self.level_blocks.append(
                        build_flat_wall(self, x, z,
                                        self.tiles["platformIndustrial_095"],
                                        False,
                                        ))
                elif col == "-":
                    door = build_flat_wall(
                        self, x, z,
                        self.tiles["platformIndustrial_095"],
                        True
                    )
                    self.level_blocks.append(door)
                elif col == "@":
                    self.player.position = item_place(x, z)
                elif col == "!":
                    npc_place = item_place(x, z)

                    baddie = npcs.Npc(
                        texture = self.sprites['mguard_s_1'],
                        parent = self,
                        x = npc_place[0],
                        y = (CUBE_SIZE / 2),
                        z = npc_place[2],
                        rotation = Vec3(0,0,0),
                        scale = (CUBE_SIZE, CUBE_SIZE -0.1, 0.1),
                    )
        
        len_rows += 1
        len_cols += 1
        floor_units = max(len_rows, len_cols)
        floor_size = floor_units * CUBE_SIZE
        floor_point = ((floor_units * CUBE_SIZE) - HALF_CUBE_SIZE) / 2

        print("floor_size", floor_size, len_rows, len_cols)

        floor = Entity(
            model='plane', scale=floor_size, color=color.yellow.tint(-.2), texture='white_cube', 
            texture_scale=(floor_size, floor_size), collider='box', parent=self.parent, 
            x = floor_point, z = floor_point, y = 0
            )

