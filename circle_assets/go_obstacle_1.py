from engine.objects.game_object import GameObject
from engine.utility.vector      import Vector
from engine.display.colors      import bcolors
import logging

class GOObstacle1(GameObject):
    def user_init(self):
        self.use_gravity  = False
        self.world_static = True
        self.collision    = True
        self.color        = bcolors.white
        self.width        = 7
        self.height       = 5

    def init(self, widhth, height):
        self.width  = widhth
        self.height = height

        self.set_model()
        self.set_colider()
        self.set_normal()

    def set_colider(self):
        col = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(True)
            col.append(row)

        self.collider = [
            col
        ]
    def set_model(self):
        model = []
        for i in range(self.height):
            row = "-" if i == 0 or i == self.height -1 else "|"
            for j in range(self.width - 2):
                row += "-" if i == 0 or i == self.height -1 else " "
            row += "-" if i == 0 or i == self.height -1 else "|"
            model.append(row)

        self.model = [
            model
        ]

    def set_normal(self):
        normal = []
        for i in range(self.height):
            row = [Vector(-1, 0)]

            for j in range(self.width - 2):
                if i / float(self.height) < 0.5:
                    row += [Vector(0, -1)]
                else:
                    row += [Vector(0, 1)]
                #if i == 0:
                #    row += [Vector(0, -1)]
                #elif i == self.height - 1:
                #    row += [Vector(0, 1)]
                #else:
                #    row += [Vector(0, 0)]

            row += [Vector(1, 0)]
            normal.append(row)
        self.normal = [
            normal
        ]
