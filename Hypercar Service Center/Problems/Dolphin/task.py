class Mammal:
    def __init__(self):
        self.bio_class = "mammal"

    def greet(self):
        print("I am a {}!".format(self.bio_class))


class Dolphin(Mammal):

    def __init__(self):
        super().__init__()

    def greet(self):
        super().greet()
        print("I am a dolphin!")
