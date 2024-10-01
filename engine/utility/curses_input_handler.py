
class CursesInuputHandler:
    def __init__(self, window = None):
        self.window = window
        self.binds = []

    def set_window(self, window):
        self.window = window

    def check_inputs(self):
        c = self.window.getch()
        for i in self.binds:
            if ord(i["char"]) == c:
                i["fun"]()

    def bind_input(self, char, obj, fun):
        self.binds.append({"char": char, "obj": obj, "fun": fun})
    def unbind_input(self, char, obj):
        pass
