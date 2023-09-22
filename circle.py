#!/usr/bin/env python3

from engine.engine                  import Engine
from circle_assets.go_circle        import GOCircle
from circle_assets.go_circle_p2     import GOCircleP2
from engine.utility.vector          import Vector
from engine.utility.collision_enums import CollisionModes as CM

if __name__ == "__main__":
    e = Engine()

    circle_1 = GOCircle(e)
    circle_2 = GOCircleP2(e)
    circle_1.velocity = Vector(10,  10)
    circle_1.position = Vector(1,   1)
    circle_1.set_model()
    circle_2.velocity = Vector(-10, 10)
    circle_2.position = Vector(173, 1)
    circle_2.collision_mode = CM.exact
    circle_2.set_model()
    e.add_object(circle_1)
    e.add_object(circle_2)
    e.set_res(height = 40)
    e.start()
