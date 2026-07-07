from .interpreter import *

class create():
    def __init__(self, args):
        with open(f"{args[1]}.easii", "w") as f:
            pass

class run():
    def __init__(self, command):
        filename = command
        inte = interpret(filename)
        inte.read()
        inte.format()
        inte.loop()