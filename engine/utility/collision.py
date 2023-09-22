#from engine.utility.vector import Vector

class Collision:
    def __init__(self, obj_1 = None, obj_2 = None, col_type = "", col_dir = 0):
        # primary object
        self.obj_1    = obj_1
        # secondary object
        self.obj_2    = obj_2
        # type, ENUM options include:
        #   engine.utility.collision_enums.world
        #   engine.utility.collision_enums.static
        #   engine.utility.collision_enums.dynamic
        self.col_type = col_type
        # directon, ENUM options include:
        #   engine.utility.collision_enums.right
        #   engine.utility.collision_enums.top
        #   engine.utility.collision_enums.left
        #   engine.utility.collision_enums.bottom
        self.col_dir  = col_dir
