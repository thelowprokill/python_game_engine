from engine.objects.game_manager    import GameManager
from engine.engine                  import Engine
from circle_assets.go_circle        import GOCircle
from circle_assets.go_obstacle_1    import GOObstacle1
from engine.utility.vector          import Vector
from engine.utility.collision_enums import CollisionModes as CM
from engine.display.colors          import bcolors

from datetime                       import datetime
import curses
import logging

class GMGameManager(GameManager):
    def user_init_game(self):
        self.add_players()

        self.set_up_world_1()

        # game variables
        self.tag_time = datetime.now()
        self.score_time = datetime.now()
        self.player_1_score = 0
        self.player_2_score = 0
        self.player_4_score = 0
        self.player_3_score = 0
        self.it = -1

    def add_players(self):
        self.circle_1 = GOCircle(self.engine, self, pos = Vector(10, 10), vel = Vector(20, 0))
        self.circle_1.player_id = 1

        self.circle_2 = GOCircle(self.engine, self, pos = Vector(20, 10), vel = Vector(20, 0))
        self.circle_2.color = bcolors.green
        self.circle_2.player_id = 2

        self.circle_3 = GOCircle(self.engine, self, pos = Vector(30, 10), vel = Vector(20, 0))
        self.circle_3.color = bcolors.blue
        self.circle_3.player_id = 3

        self.circle_4 = GOCircle(self.engine, self, pos = Vector(40, 10), vel = Vector(20, 0))
        self.circle_4.color = bcolors.yellow
        self.circle_4.player_id = 4

        # add to engine
        self.engine.add_object(self.circle_1)
        self.engine.add_object(self.circle_2)
        self.engine.add_object(self.circle_3)
        self.engine.add_object(self.circle_4)

    def set_up_world_1(self):
        # dynamic
        self.it_start = GOCircle(self.engine, self, pos = Vector(230, 10), vel = Vector(0, 0))
        self.it_start.color = bcolors.red
        self.it_start.player_id = -1

        # static
        obstacle_1 = GOObstacle1(self.engine, self, pos = Vector(70, 4))
        obstacle_1.init(3, 10)
        obstacle_2 = GOObstacle1(self.engine, self, pos = Vector(70, 30))
        obstacle_2.init(3, 28)

        obstacle_3 = GOObstacle1(self.engine, self, pos = Vector(140, 4))
        obstacle_3.init(3, 5)
        obstacle_4 = GOObstacle1(self.engine, self, pos = Vector(140, 25))
        obstacle_4.init(3, 10)
        obstacle_5 = GOObstacle1(self.engine, self, pos = Vector(140, 51))
        obstacle_5.init(3, 7)

        obstacle_6 = GOObstacle1(self.engine, self, pos = Vector(210, 4))
        obstacle_6.init(3, 25)
        obstacle_7 = GOObstacle1(self.engine, self, pos = Vector(210, 45))
        obstacle_7.init(3, 13)

        obstacle_8 = GOObstacle1(self.engine, self, pos = Vector(74, 30))
        obstacle_8.init(66, 3)

        self.engine.add_object(self.it_start)
        self.engine.add_static_object(obstacle_1)
        self.engine.add_static_object(obstacle_2)
        self.engine.add_static_object(obstacle_3)
        self.engine.add_static_object(obstacle_4)
        self.engine.add_static_object(obstacle_5)
        self.engine.add_static_object(obstacle_6)
        self.engine.add_static_object(obstacle_7)
        self.engine.add_static_object(obstacle_8)

    def tick(self, dt):
        now = datetime.now()
        if (now - self.score_time).total_seconds() > 5:
            #logging.info(f"player 1 score: {self.player_1_score}")
            #logging.info(f"player 2 score: {self.player_2_score}")
            #logging.info(f"player 3 score: {self.player_3_score}")
            #logging.info(f"player 4 score: {self.player_4_score}")
            self.score_time = now
            if self.it == 1:
                self.player_1_score += 1
            elif self.it == 2:
                self.player_2_score += 1
            elif self.it == 3:
                self.player_3_score += 1
            elif self.it == 4:
                self.player_4_score += 1


    def user_init_inputs(self):
        self.engine.input_handler.bind_input("h", self.circle_1, self.circle_1.jump)
        self.engine.input_handler.bind_input("j", self.circle_2, self.circle_2.jump)
        self.engine.input_handler.bind_input("k", self.circle_3, self.circle_3.jump)
        self.engine.input_handler.bind_input("l", self.circle_4, self.circle_4.jump)

    def tag(self, player_id, it):
        if self.it == -1:
            self.engine.remove_object(self.it_start)

        new_tag = datetime.now()
        if (new_tag - self.tag_time).total_seconds() > 1:
            logging.info(f"{player_id} taged {it}")
            self.it = it
            if it == 1:
                self.player_1_score += 1
            elif it == 2:
                self.player_2_score += 1
            elif it == 3:
                self.player_3_score += 1
            elif it == 4:
                self.player_4_score += 1
            self.tag_time = new_tag
            self.score_time = new_tag

    def render(self, window):
        window.addstr(0, 2, f"Player 1 Score: {self.player_1_score}")
        window.addstr(0, self.engine.display.width - len(f"Player 2 Score: {self.player_2_score}") - 2, f"Player 2 Score: {self.player_2_score}", curses.color_pair(bcolors.green))
        window.addstr(2, 2, f"Player 3 Score: {self.player_3_score}", curses.color_pair(bcolors.blue))
        window.addstr(2, self.engine.display.width - len(f"Player 4 Score: {self.player_4_score}") - 2, f"Player 4 Score: {self.player_4_score}", curses.color_pair(bcolors.yellow))
