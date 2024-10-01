from engine.objects.game_object import GameObject
from engine.utility.vector      import Vector

class GOTank(GameObject):
    def user_init(self):
        #self.velocity     = Vector(10, 10)
        #self.use_gravity  = True
        self.world_static = False
        self.collision    = True
        self.frame        = 0

    def user_collision(self, collision):
        pass

    def user_init_inputs(self):
        self.engine_ref.input_handler.bind_input("w", self, self.move_up)
        self.engine_ref.input_handler.bind_input("a", self, self.move_left)
        self.engine_ref.input_handler.bind_input("s", self, self.move_down)
        self.engine_ref.input_handler.bind_input("d", self, self.move_right)

    def move_up(self):
        if self.positon.y > 1:
            self.position.y -= 1
            self.frame = 0
    def move_down(self):
        if self.position.y < self.engine_ref.display.height - 6:
            self.position.y += 1
            self.frame = 0
    def move_left(self):
        if self.position.x > 1:
            self.position.x -= 1
            self.frame = 1
    def move_right(self):
        if self.position.x < self.engine_ref.display.width - 11:
            self.position.x += 1
            self.frame = 1

    def set_colider(self):
        self.collider = [
          [True, True,  True,  True,  True,  True,  True ],
          [True, False, False, False, False, False, True ],
          [True, False, False, False, False, False, True ],
          [True, False, False, False, False, False, True ],
          [True, True,  True,  True,  True,  True,  True ],
        ]
        
    def set_model(self):
        """
        []___[]   
        []   []
        []   []
        []___[]
        []   []

         ________
        |________|
         _|____|_
        |________|

        """

        self.model = [
            [
              ["[",  "]", "_", "_", "_", "[", "]" ],
              ["[",  "]", "",  "",  "",  "[", "]" ],
              ["[",  "]", "",  "",  "",  "[", "]" ],
              ["[",  "]", "_", "_", "_", "[", "]" ],
              ["[",  "]", "",  "",  "",  "[", "]" ],
            ]
            [
              ["",  "_", "_", "_", "_", "_", "_", "_", "_", ""  ],
              ["|", "_", "_", "_", "_", "_", "_", "_", "_", "|" ],
              ["",  "_", "|", "_", "_", "_", "_", "|", "_", ""  ],
              ["",  "_", "_", "_", "_", "_", "_", "_", "_", ""  ],
              ["|", "_", "_", "_", "_", "_", "_", "_", "_", "|" ],
            ]
        ]
