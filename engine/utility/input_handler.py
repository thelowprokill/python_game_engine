import sys
import select
import tty
import termios


class InputHandler:
    def __init__(self):
        tty.setcbreak(sys.stdin.fileno())
        self.old_settings = termios.tcgetattr(sys.stdin)
        self.inputs = []

    def close(self):
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

    def isData(self):
        return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])
    
    def get_input(self):
        try:
            if self.isData():
                return sys.stdin.read(1)
                #if c == '\x1b':         # x1b is ESC
                #    break
        
        except Exception as e:
            print(e)
         #finally:
         #    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

    def check_inputs(self):
        c = self.get_input()
        #print(c)
        for i in self.inputs:
            if i["char"] == c:
                i["fun"]()

    def bind_input(self, char, obj, fun):
        self.inputs.append({"char": char, "obj": obj, "fun": fun})

    def unbind_input(self, char, obj):
        for i in self.inputs:
            if i["char"] == char and i["obj"] == obj:
                self.inputs.remove(i)

    def clear_inputs(self):
        self.inputs = []

