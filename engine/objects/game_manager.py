from engine.engine                  import Engine

class GameManager:
    def __init__(self):
        self.engine = Engine(self)

        self.user_init_game()
        self.user_init_inputs()

    def start(self):
        self.engine.start()

    def tick(self, dt):
        pass

    def user_init_game(self):
        pass
    def user_init_inputs(self):
        pass

    def render(self, window):
        pass
