from circle_assets.go_circle import GOCircle
from engine.utility.vector   import Vector

class GOCircleP2(GOCircle):
    def user_init(self):
        self.obj_name     = "B"
        self.velocity     = Vector(10, 10)
        self.use_gravity  = True
        self.world_static = False
        self.collision    = True

    def user_init_inputs(self):
        self.engine_ref.input_handler.bind_input("e", self, self.jump)
