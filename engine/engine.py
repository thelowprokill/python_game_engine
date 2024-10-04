#!/usr/bin/env python3

import logging

import os
import time

from curses import wrapper

from engine.display.display              import Display
from engine.utility.collision            import Collision
from engine.utility.collision_enums      import CollisionModes as CM, CollisionTypes as CT, CollisionDirection as CD
from engine.utility.input_handler        import InputHandler
from engine.utility.curses_input_handler import CursesInuputHandler

class Engine:
    def __init__(self, game_manager, fps = 60):
        logging.basicConfig(filename="logs/engine.log", level=logging.INFO)
        self.display         = Display()
        self.max_fps         = fps
        self.fps_frames      = 0
        self.fps_int         = 0.25
        self.fps             = self.max_fps
        self.world_collision = True
        self.obj_collision   = True

        self.paused          = True
        self.running         = True

        self.dynamic_objects = []
        self.static_objects  = []
        self.game_manager    = game_manager
        self.input_handler   = InputHandler()
        self.curses_input    = CursesInuputHandler()


        logging.info(f"Engine initialized, running at {self.max_fps} FPS")

        wrapper(self.init_engine)

    def init_engine(self, stdscr):
        self.window = stdscr
        self.display.set_window(stdscr)
        self.curses_input.set_window(stdscr)
        stdscr.nodelay(True)

    def set_res(self, width = None, height = None):
        self.display.width  = width  if width  is not None else self.display.width
        self.display.height = height if height is not None else self.display.height

    def start(self):
        logging.info("Engine started")
        self.fps_time   = time.time()
        self.start_time = time.time()
        self.last_time  = time.time()
        self.next_time  = time.time()

        i = 0
        while self.running:
            self.next_time = time.time()
            dt = self.next_time - self.last_time
            self.input_handler.check_inputs()
            self.curses_input.check_inputs()

            if not self.paused:
                i += 1
                self.tick(dt)

            else:
                self.display.draw(self.dynamic_objects + self.static_objects + [self.game_manager])

            self.calculate_frame_rate()
            self.limit_frame_rate()
            self.last_time = self.next_time
        self.end_time = time.time()

    def quit(self):
        self.running = False

    def tick(self, dt):
        for o in self.dynamic_objects:
            o.tick(dt)

        self.game_manager.tick(dt)

        self.check_collision()

        try:
            self.display.draw(self.dynamic_objects + self.static_objects + [self.game_manager])
        except Exception as e:
            logging.error(f"Exception in draw: {e}")

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
            for obj_1 in self.dynamic_objects:
                for obj_2 in self.dynamic_objects + self.static_objects:
                    if obj_2 != obj_1:
                        if obj_1.check_overlap(obj_2):
                            obj_1.dynamic_collision(Collision(obj_1 = obj_1, obj_2 = obj_2, col_type = CT.dynamic))
        
    def add_object(self, obj):
        try:
            self.dynamic_objects.append(obj)
        except Exception as e:
            logging.error(f"Exception in add_object: {e}")

    def remove_object(self, obj):
        try:
            self.dynamic_objects.remove(obj)
        except Exception as e:
            logging.error(f"Exception in remove_object: {e}").dynamic_objects.remove(obj)
        
    def add_static_object(self, obj):
        try:
            obj.world_static = True
            self.static_objects.append(obj)
        except Exception as e:
            logging.error(f"Exception in add_static_object: {e}")

    def remove_static_object(self, obj):
        try:
            self.static_objects.remove(obj)
        except Exception as e:
            logging.error(f"Exception in remove_static_object: {e}")

    def clear_objects(self):
        self.dynamic_objects = []
        self.static_objects  = []

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
