from engine.objects.game_object import GameObject
from engine.utility.vector      import Vector

class GOCircle(GameObject):
    def user_init(self):
        self.obj_name     = "A"
        self.velocity     = Vector(10, 10)
        self.use_gravity  = True
        self.world_static = False
        self.collision    = True

    def user_collision(self, collision):
        pass

    def user_init_inputs(self):
        self.engine_ref.input_handler.bind_input("w", self, self.jump)

    def jump(self):
        self.velocity.y = -9.81

    def set_colider(self):
        self.collider = [
          [False, True,  True,  True,  True,  False],
          [True,  False, False, False, False, True ],
          [True,  False, False, False, False, True ],
          [True,  False, False, False, False, True ],
          [True,  False, False, False, False, True ],
          [False, True,  True,  True,  True,  False]
        ]
        
    def set_model(self):
        self.model = [
            [
              ["",   "-", "-", "-", "-", ""  ],
              ["/",  "",  "",  "",  "",  "\\"],
              ["|",  "",  self.obj_name,  "",  "",  "|" ],
              ["|",  "",  "",  "",  "",  "|" ],
              ["\\", "",  "",  "",  "",  "/" ],
              ["",   "-", "-", "-", "-", ""  ]
            ]
        ]
