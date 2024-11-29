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
        self.new_game()

    def new_game(self):
        # game variables
        #self.engine.input_handler.clear_inputs()

        self.tag_time          = datetime.now()
        self.score_time        = datetime.now()
        self.player_1_score    = 0
        self.player_2_score    = 0
        self.player_4_score    = 0
        self.player_3_score    = 0
        self.it                = -1
        self.victory_threshold = 25
        self.player_colors     = [bcolors.white, bcolors.green, bcolors.blue, bcolors.yellow]
        self.player_controls   = ["a", "", "", "l"]
        self.players           = []
        self.scores            = []
        self.game_over         = False
        self.victor            = 0

        self.engine.clear_objects()

        self.user_init_inputs()

        self.add_players()

        self.set_up_world_1()

    def add_players(self):
        i = 1
        self.players = []
        for color, control in zip(self.player_colors, self.player_controls):
            circle = GOCircle(self.engine, self, pos = Vector(10 * i, 10), vel = Vector(20, 0))
            circle.player_id = i
            circle.color = color
            self.engine.input_handler.bind_input(control, circle, circle.jump)
            self.players.append(circle)
            self.engine.add_object(circle)

            circle = GOCircle(self.engine, self, pos = Vector(self.engine.display.width - 10 * (len(self.player_colors) - i + 1), 10), vel = Vector(-20, 0))
            circle.player_id = i
            circle.color = color
            self.engine.input_handler.bind_input(control, circle, circle.jump)
            self.players.append(circle)
            self.engine.add_object(circle)
            i += 1

        self.scores = []
        for _ in range(len(self.players)):
            self.scores.append(0)

    def set_up_world_1(self):
        # dynamic
        self.it_start = GOCircle(self.engine, self, pos = Vector(105, 40), vel = Vector(0, 0))
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
        #self.engine.add_static_object(obstacle_6)
        self.engine.add_static_object(obstacle_7)
        self.engine.add_static_object(obstacle_8)

    def victory(self, victor):
        self.engine.pause()

        lossers = []
        for p in self.players:
            if p.player_id != victor:
                lossers.append(p)
                self.engine.remove_object(p)

        self.game_over = True
        self.engine.input_handler.clear_inputs()
        self.engine.input_handler.bind_input(" ", self,        self.new_game)
        self.engine.input_handler.bind_input("q", self.engine, self.engine.quit)
        self.victor = victor

    def tick(self, dt):
        now = datetime.now()
        if (now - self.score_time).total_seconds() > 5:
            self.score_time = now
            
            if self.it > 0:
                self.scores[self.it - 1] += 1
                if self.scores[self.it - 1] >= self.victory_threshold:
                    self.victory(self.it)

    def pause(self):
        self.engine.input_handler.bind_input("q", self.engine, self.engine.quit)
        self.engine.input_handler.bind_input("n", self,        self.new_game)
        self.engine.pause()

    def resume(self):
        self.engine.input_handler.unbind_input("q", self.engine)
        self.engine.input_handler.unbind_input("n", self)
        self.engine.resume()

    def user_init_inputs(self):
        self.engine.input_handler.bind_input("\x1b", self, self.pause)
        self.engine.input_handler.bind_input(" ",    self, self.resume)

    def tag(self, player_id, it):
        if self.it == -1:
            self.engine.remove_object(self.it_start)

        new_tag = datetime.now()
        if (new_tag - self.tag_time).total_seconds() > 1:
            logging.info(f"{player_id} taged {it}")
            self.it = it
            self.scores[it - 1] += 1
            if self.scores[it - 1] >= self.victory_threshold:
                self.victory(it)
            self.tag_time = new_tag
            self.score_time = new_tag

    def render(self, window):
        if self.game_over:
            window.addstr(20, 20, f"Player {self.victor} is Victorious! Score: {self.scores[self.victor - 1]}!", curses.color_pair(self.player_colors[self.victor - 1]))

        window.addstr(0, 2, f"Player 1 Score: {self.scores[0]}")
        window.addstr(0, self.engine.display.width - len(f"Player 2 Score: {self.scores[1]}") - 2, f"Player 2 Score: {self.scores[1]}", curses.color_pair(bcolors.green))
        window.addstr(2, 2, f"Player 3 Score: {self.scores[2]}", curses.color_pair(bcolors.blue))
        window.addstr(2, self.engine.display.width - len(f"Player 4 Score: {self.scores[3]}") - 2, f"Player 4 Score: {self.scores[3]}", curses.color_pair(bcolors.yellow))

        #window.addstr(1, int(self.engine.display.width / 2) - int(len(f"FPS: {self.engine.fps}") / 2), f"{self.engine.display.width}", f"FPS: {self.engine.fps}")
        window.addstr(2, int(self.engine.display.width / 2 - len(f"FPS: {self.engine.fps}") / 2), f"FPS: {self.engine.fps}")
