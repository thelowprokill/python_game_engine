from engine.objects.game_object import GameObject
from engine.utility.vector      import Vector
from engine.display.colors      import bcolors

class GOCircle(GameObject):
    def user_init(self):
        self.use_gravity  = True
        self.world_static = False
        self.collision    = True
        self.color        = bcolors.red

    def dynamic_collision(self, collision):
        super().dynamic_collision(collision)
        if collision.obj_1 is not None and collision.obj_2 is not None and collision.obj_1 == self:
            if self.player_id == self.game_manager.it and collision.obj_2.player_id != 0:
                self.game_manager.tag(self.player_id, collision.obj_2.player_id)

    def set_colider(self):
        self.collider = [
            [
                [False, True,  True,  True,  True,  False],
                [True,  False, False, False, False, True ],
                [True,  False, False, False, False, True ],
                [True,  False, False, False, False, True ],
                [True,  False, False, False, False, True ],
                [False, True,  True,  True,  True,  False]
            ]
        ]
        
    def set_model(self):
        self.model = [
            [
              " ---- ",
              "/    \\",
              "| It |",
              "|    |",
              "\\    /",
              " ---- "
            ]
        ]

    def set_normal(self):
        self.normal = [
            [
                [Vector(-1, 0), Vector(0, -1),  Vector(0, -1), Vector(0, -1), Vector(0, -1), Vector(1, 0)],
                [Vector(-1, 0), Vector(),       Vector(),      Vector(),      Vector(),      Vector(1, 0)],
                [Vector(-1, 0), Vector(),       Vector(),      Vector(),      Vector(),      Vector(1, 0)],
                [Vector(-1, 0), Vector(),       Vector(),      Vector(),      Vector(),      Vector(1, 0)],
                [Vector(-1, 0), Vector(),       Vector(),      Vector(),      Vector(),      Vector(1, 0)],
                [Vector(-1, 0), Vector(0, 1),   Vector(0, 1),  Vector(0, 1),  Vector(0, 1),  Vector(1, 0)],
            ]
        ]
