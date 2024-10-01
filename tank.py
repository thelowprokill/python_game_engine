#!/usr/bin/env python3

from engine.engine                  import Engine
#from circle_assets.go_circle        import GOCircle
from tank_assets.go_tank            import GOTank
#from circle_assets.go_circle_p2     import GOCircleP2
from engine.utility.vector          import Vector
from engine.utility.collision_enums import CollisionModes as CM

if __name__ == "__main__":
    e = Engine()

    tank_1 = GOTank(e, pos = Vector(1, 1))
    tank_1.set_model()
    #circle_1 = GOCircle(e, pos = Vector(1, 1), vel = Vector(10, 10))
    #circle_1.set_model()

    #circle_2 = GOCircleP2(e, pos = Vector(173, 1), vel = Vector(-10, 10))
    #circle_2.set_model()
    ##circle_2.collision_mode = CM.exact
    #e.add_object(circle_1)
    #e.add_object(circle_2)
    e.add_object(tank_1)
    e.set_res(height = 40)
    e.start()
