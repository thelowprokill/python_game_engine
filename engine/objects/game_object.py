from engine.utility.vector          import Vector
from engine.utility.collision       import Collision
from engine.utility.collision_enums import CollisionModes as CM, CollisionTypes as CT, CollisionDirection as CD
import curses
import logging

#################################################
# class:   GameObject                           #
# purpose: base class for game objects to       #
#   inherit                                     #
# author:  Jon Hull 29 July 2023                #
#################################################
class GameObject:
    #############################################
    # fun: __init__/1                           #
    # purpose: initializer for game object      #
    # overwriteable: False                      #
    #############################################
    def __init__(self, e, gm, pos = Vector(1, 1), vel = Vector()):
        self.engine_ref     = e
        self.game_manager   = gm
        self.last_position  = pos
        self.position       = pos
        self.z              = 0
        self.player_id      = 0

        self.color          = 0

        self.on_screen      = False

        self.gravity        = Vector(0, 9.81)
        self.velocity       = vel

        self.use_gravity    = False
        self.world_static   = True
        self.collision      = False
        self.collision_mode = CM.exact

        self.mass           = 1
        self.r              = 1

        self.frame  = 0
        self.frames = 0
        self.frames_per_frame = 0

        self.user_init_inputs()

        self.user_init()

        self.set_model()
        self.set_colider()
        self.set_normal()

    #############################################
    # fun: user_init/1                          #
    # purpose: user initialzation               #
    # overwriteable: True                       #
    #############################################
    def user_init(self):
        pass

    #############################################
    # fun: user_init_inputs/1                   #
    # purpose: user input initialzation         #
    # overwriteable: True                       #
    #############################################
    def user_init_inputs(self):
        pass

    #############################################
    # fun: user_tick/2                          #
    # purpose: user tick this function is       #
    #   called ever frame                       #
    # overwriteable: True                       #
    #############################################
    def user_tick(self, dt):
        pass

    #############################################
    # fun: dynamic_collision/2                  #
    # purpose: handle what happens when a       #
    #   colision happens                        #
    # overwriteable: True                       #
    #############################################
    def dynamic_collision(self, collision):
        if self.collision and collision.obj_1 is not None and collision.obj_2 is not None:
            if collision.obj_1 == self or collision.obj_2 == self:
                obj = collision.obj_1 if collision.obj_1 != self else collision.obj_2

                normal = obj.find_normal(collision)#.normalize()

                vel = self.velocity
                v1 = vel.t_sub(normal.t_mult(2 * normal.dot(vel)))

                #logging.info(f"Collision between {collision.obj_1.player_id} and {collision.obj_2.player_id}")
                #logging.info(f"V0: {vel.x}, {vel.y}")
                #logging.info(f"V1: {v1.x}, {v1.y}")
                #logging.info(f"Normal: {normal.x}, {normal.y}")

                self.velocity = v1

    def find_normal(self, collision):
        obj = None
        normal = Vector(0, 0)
        if self == collision.obj_1:
            obj = collision.obj_2
        elif self == collision.obj_2:
            obj = collision.obj_1
        if obj is not None:
            for y in range(len(self.normal[self.frame])):
                for x in range(len(self.normal[self.frame][y])):
                    if self.collider[self.frame][y][x] and obj.check_collision(int(self.position.x) + x, int(self.position.y) + y):
                        normal = self.normal[self.frame][y][x]
                        if normal != Vector(0, 0):
                            return normal
        return normal

    #############################################
    # fun: world_collision/4                    #
    # purpose: handle what happens when a       #
    #   colision happens                        #
    # overwriteable: True                       #
    #############################################
    def world_collision(self, collision, x, y):
        if self.collision:
            if self.collision_mode == CM.exact and collision.col_type == CT.world and collision.col_dir in CD:
                if   collision.col_dir == CD.right and self.velocity.x > 0:
                    self.velocity.x *= -1
                    self.position.x = x - (self.position.x + self.collider_width() - x) - self.collider_width()
                elif collision.col_dir == CD.left  and self.velocity.x < 0:
                    self.velocity.x *= -1
                    self.position.x *= -1
                elif collision.col_dir == CD.down  and self.velocity.y > 0:
                    self.velocity.y *= -1
                    self.position.y = y - (self.position.y + self.collider_height() - y) - self.collider_height()
                elif collision.col_dir == CD.up    and self.velocity.y < 0:
                    self.velocity.y *= -1
                    self.position.y *= -1
                    self.position.y += 3
            if self.collision_mode == CM.quick and collision.col_type == CT.world and collision.col_dir in CD:
                if   collision.col_dir == CD.right and self.velocity.x > 0:
                    self.velocity.x *= -1
                elif collision.col_dir == CD.left  and self.velocity.x < 0:
                    self.velocity.x *= -1
                elif collision.col_dir == CD.down  and self.velocity.y > 0:
                    self.velocity.y *= -1
                elif collision.col_dir == CD.up    and self.velocity.y < 0:
                    self.velocity.y *= -1

    #############################################
    # fun: draw/3                               #
    # purpose: returns the part of the model at #
    #   x, y in the current frame, and the z    #
    #   index                                   #
    # overwriteable: True                       #
    #############################################
    def draw(self, x, y):
        x = x - int(self.position.x)
        y = y - int(self.position.y)

        if x >= 0 and x < self.width() and y >= 0 and y < self.height():
            return (self.model[self.frame][y][x], self.z, self.color)
        else:
            return ("", -1, None)

    def render(self, window):
        x = int(self.position.x)
        y = int(self.position.y)
        for l in self.model[self.frame]:
            if y >= 0 and y < self.engine_ref.display.height and x >= 0 and x < self.engine_ref.display.width - len(l):
                window.addstr(y, int(self.position.x), l, curses.color_pair(self.color))
            y += 1

    #############################################
    # fun: set_model/1                          #
    # purpose: sets up the current model,       #
    #   this function should be overwritten     #
    # overwriteable: True                       #
    #############################################
    def set_model(self):
        self.model = [
            [ ["A"] ]
        ]
    #############################################
    # fun: set_collider/1                       #
    # purpose: sets up the current colider,     #
    #   this function should be overwritten     #
    # overwriteable: True                       #
    #############################################
    def set_collider(self):
        self.model = [
            [True]
        ]

    def set_normal(self):
        self.normal = [
            [Vector(0, 0)]
        ]

    #############################################
    # fun: tick/2                               #
    # purpose: update position based on         #
    #   velocity update velocity based on       #
    #   acceleration, this is where the physics #
    #   and animations are updated              #
    # overwriteable: False                      #
    #############################################
    def tick(self, dt):
        # physics
        if not self.world_static:
            if self.use_gravity:
                self.velocity.add(self.gravity.t_mult(dt))

            self.position.add(self.velocity.t_mult(dt))
            self.last_position = self.position

        #update anim
        if self.frames > self.frames_per_frame and self.frames_per_frame > 0:
            self.frames = 1
            self.frame += 1
            if self.frame >= len(self.model):
                self.frame = 0
        else:
            self.frames += 1

        self.user_tick(dt)

    #############################################
    # fun: check_collision/3                    #
    # purpose: checks for collision with other  #
    #   objects and world static                #
    # overwriteable: False                      #
    #############################################`
    def check_collision(self, x, y):
        # need to calculate collision between frames so that the ball bounces correctly
        #if self.position.y > 41 and self.velocity.y > 0:
        #    self.velocity.y *= -1
        x = x - int(self.position.x)
        y = y - int(self.position.y)

        if self.in_bounding_box(x, y):
            return self.collider[self.frame][y][x]
        else:
            return False

    def check_overlap(self, obj):
        l1_x = self.position.x
        l1_y = self.position.y
        r1_x = self.position.x + self.collider_width()
        r1_y = self.position.y + self.collider_height()

        l2_x = obj.position.x
        l2_y = obj.position.y
        r2_x = obj.position.x + obj.collider_width()
        r2_y = obj.position.y + obj.collider_height()

        if l1_x == r1_x or l1_y == r1_y or l2_x == r2_x or l2_y == r2_y:
            return False
        if l1_x > r2_x or l2_x > r1_x:
            return False
        if r1_y < l2_y or r2_y < l1_y:
            return False
        return True

    #############################################
    # fun: check_world_collision/3              #
    # purpose: checks for collision with world  #
    #   border                                  #
    # overwriteable: False                      #
    #############################################`
    def check_world_collision(self, x, y):
        # need to calculate collision between frames so that the ball bounces correctly
        #if self.position.y > 41 and self.velocity.y > 0:
        #    self.velocity.y *= -1

        if self.collision:
            if self.position.x <= 1:
                self.world_collision(Collision(obj_1 = self, col_type = CT.world, col_dir = CD.left),  x, y)
            elif self.position.x + self.collider_width() >= x:
                self.world_collision(Collision(obj_1 = self, col_type = CT.world, col_dir = CD.right), x, y)
            if self.position.y <= 4:
                self.world_collision(Collision(obj_1 = self, col_type = CT.world, col_dir = CD.up),    x, y)
            elif self.position.y + self.collider_height() >= y:
                self.world_collision(Collision(obj_1 = self, col_type = CT.world, col_dir = CD.down),  x, y)


    #############################################
    # fun: width/1                              #
    # purpose: gets the width of the current    #
    #   anim frame                              #
    # overwriteable: False                      #
    #############################################
    def width(self):
        return len(self.model[self.frame][0])
    #############################################
    # fun: height/1                             #
    # purpose: gets the height of the current   #
    #   anim frame                              #
    # overwriteable: False                      #
    #############################################
    def height(self):
        return len(self.model[self.frame])

    #############################################
    # fun: collider_width/1                     #
    # purpose: gets the width of the current    #
    #   anim frame                              #
    # overwriteable: False                      #
    #############################################
    def collider_width(self):
        return len(self.collider[self.frame][0])
    #############################################
    # fun: collider_height/1                    #
    # purpose: gets the height of the current   #
    #   anim frame                              #
    # overwriteable: False                      #
    #############################################
    def collider_height(self):
        return len(self.collider[self.frame])
    #############################################
    # fun: in_bounding_box/3                    #
    # purpose: gets the height of the current   #
    #   anim frame                              #
    # overwriteable: False                      #
    #############################################
    def in_bounding_box(self, x, y):
        return x >= 0 and x < self.collider_width() and y >= 0 and y < self.collider_height()

