#!/usr/bin/env python3

import os
import time

from curses import wrapper

from engine.display.display              import Display
from engine.utility.collision            import Collision
from engine.utility.collision_enums      import CollisionModes as CM, CollisionTypes as CT, CollisionDirection as CD
from engine.utility.input_handler        import InputHandler
from engine.utility.curses_input_handler import CursesInuputHandler

class Engine:
    def __init__(self, fps = 15):
        self.display         = Display()
        self.max_fps         = fps
        self.fps_frames      = 0
        self.fps_int         = 0.25
        self.fps             = self.max_fps
        self.world_collision = True
        self.obj_collision   = True

        self.paused          = False

        self.dynamic_objects = []
        self.static_objects  = []
        self.input_handler   = InputHandler()
        self.curses_input    = CursesInuputHandler()

        #self.input_handler.bind_input("\x1b", self, self.pause)
        #self.input_handler.bind_input(" ",    self, self.resume)
        #self.curses_input.bind_input("\x1b", self, self.pause)
        self.curses_input.bind_input(" ",    self, self.resume)

    def set_res(self, width = None, height = None):
        self.display.width  = width  if width  is not None else self.display.width
        self.display.height = height if height is not None else self.display.height

    def start(self):
        wrapper(self.run)

    def run(self, stdscr):
        self.fps_time   = time.time()
        self.start_time = time.time()
        self.last_time  = time.time()
        self.next_time  = time.time()

        self.display.set_window(stdscr)
        self.curses_input.set_window(stdscr)
        stdscr.nodelay(True)

        i = 0
        while i < 800:
            self.next_time = time.time()
            dt = self.next_time - self.last_time
            self.input_handler.check_inputs()
            self.curses_input.check_inputs()

            if not self.paused:
                i += 1
                #self.clear_screen()
                #print("FPS: {}".format(self.fps))

                #self.display.tick(dt)
                self.tick(dt)

            else:
                #self.clear_screen()
                self.display.draw(self.dynamic_objects + self.static_objects)
            #print(self.paused)

            self.calculate_frame_rate()
            self.limit_frame_rate()
            self.last_time = self.next_time
        self.end_time = time.time()

    def tick(self, dt):
        for o in self.dynamic_objects:
        #    o.input(c)
            o.tick(dt)

        self.check_collision()

        self.display.draw(self.dynamic_objects + self.static_objects)

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

    def check_collision(self):
        # world collision
        if self.world_collision:
            for obj in self.dynamic_objects:
                obj.check_world_collision(self.display.width, self.display.height)

        if self.obj_collision:
            collisions = []
            for obj in self.dynamic_objects:
                for obj_2 in self.dynamic_objects:
                    if obj_2 != obj and (obj_2, obj) not in collisions:
                        #print("Test collision")
                        if obj.check_overlap(obj_2):
                            obj.dynamic_collision(Collision(obj_1 = obj, obj_2 = obj_2, col_type = CT.dynamic))
                            obj_2.dynamic_collision(Collision(obj_1 = obj_2, obj_2 = obj, col_type = CT.dynamic))
                            #print("Collision")
                        else:
                            pass
                            #print("No collision")
                        collisions.append((obj, obj_2))
        
    def add_object(self, obj):
        self.dynamic_objects.append(obj)
        
    def add_static_object(self, obj):
        obj.world_static = True
        self.static_objects.append(obj)

    def clear_screen(self):
        os.system("clear")
    
    def calculate_frame_rate(self):
        t = time.time()
        self.fps_frames += 1
        if t - self.fps_time > self.fps_int:
            self.fps = round(self.fps_frames / (t - self.fps_time))
            self.fps_time = t
            self.fps_frames = 0

    def limit_frame_rate(self):
        t = time.time()
        wait_time = (1. / self.max_fps) - (t - self.next_time)
        if wait_time > 0:
            time.sleep(wait_time)

if __name__ == "__main__":
    import objects.go_circle as GO
    e = Engine()
    e.display.add_object(GO.GOCircle())
    e.start()
