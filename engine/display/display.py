#!/usr/bin/env python3
class Display:
    def __init__(self):
        self.width   = 180
        self.height  = 50
        #self.objects = []
        #self.input_handler = InputHandler()

    #def add_object(self, obj):
    #    self.objects.append(obj)

    #def tick(self, dt):
    #    #c = self.input_handler.get_input()
    #    for o in self.objects:
    #    #    o.input(c)
    #        o.tick(dt)

    #    self.draw()

    def draw(self, objects):
        for y in range(self.height):
            for x in range(self.width):
                char = " "
                z_index = 0
                if y == 0 or y == self.height - 1 or x == 0 or x == self.width - 1:
                    char = "="
                else:
                    for obj in objects:
                        c, z = obj.draw(x, y)
                        if c != "" and z >= z_index:
                            char = c
                            z = z_index


                print(char, end="")
            print("")

