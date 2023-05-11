class gen1():
    def __init__(self):
        print("I am from gen1")

class gen2(gen1):

    def __init__(self):
        super().__init__()
        print("I am from gen2")

gen= gen2()
