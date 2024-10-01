from engine.objects.game_object import GameObject
from engine.utility.vector      import Vector
from engine.display.colors      import bcolors
import curses

class GOCircle(GameObject):
    def user_init(self):
        self.obj_name     = "A"
        self.it           = False
        self.use_gravity  = True
        self.world_static = False
        self.collision    = True
        self.color        = bcolors.white

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
              #["",   "-", "-", "-", "-", ""  ],
              #["/",  "",  "",  "",  "",  "\\"],
              #["|",  "",  self.obj_name,  "",  "",  "|" ],
              #["|",  "",  "",  "",  "",  "|" ],
              #["\\", "",  "",  "",  "",  "/" ],
              #["",   "-", "-", "-", "-", ""  ]
              " ---- ",
              "/    \\",
              "|    |",
              "|    |",
              "\\    /",
              " ---- "
            ]
        ]

    def render(self, window):
        super().render(window)
        
        if self.it:
            window.addstr(int(self.position.y) + 2, int(self.position.x) + 2, "It", curses.color_pair(bcolors.red))

