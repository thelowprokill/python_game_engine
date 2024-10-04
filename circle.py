#!/usr/bin/env python3

from circle_assets.gm_game_manager import GMGameManager as GM

#from engine.engine                  import Engine
#from circle_assets.go_circle        import GOCircle
#from circle_assets.go_obstacle_1    import GOObstacle1
#from engine.utility.vector          import Vector
#from engine.utility.collision_enums import CollisionModes as CM
#from engine.display.colors          import bcolors

if __name__ == "__main__":
    gm = GM()
    gm.start()

    #e = Engine()

    ## players
    #circle_1 = GOCircle(e, pos = Vector(2, 30),  vel = Vector(10, 0))
    #circle_1.set_model()

    #circle_2 = GOCircle(e, pos = Vector(60, 30), vel = Vector(-10, 0))
    #circle_2.set_model()
    #circle_2.color = bcolors.green

    #circle_2.it = True

    ## controls
    #e.input_handler.bind_input("w", circle_1, circle_1.jump)
    #e.input_handler.bind_input("e", circle_2, circle_2.jump)

    ## static
    #obstacle_1 = GOObstacle1(e, pos = Vector(70, 30))
    #obstacle_1.set_model()

    #e.add_object(circle_1)
    #e.add_object(circle_2)

    #e.add_static_object(obstacle_1)


    #e.start()
