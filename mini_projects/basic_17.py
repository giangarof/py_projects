# Create a game, using Class


class Game:
    def __init__(self):
        self.score = 0

    def result(self):
        print(f"Your score: {self.score}/5")

    def start(self):
        # results = self.result()
        q1 = int(input('how many legs a snake has?'))
        if q1 == 0:
            self.score += 1

        q2 = int(input("how many legs a dog has?"))
        if q2 == 4:
            self.score += 1

        q3 = input("what does 'js' stands for?")
        if q3 == 'javascript':
            self.score += 1

        q4 = input("which color are the clouds? ")
        if q4 == 'white':
            self.score += 1

        q5 = input("who tried to kill harry potter?")
        if q5 == "voldemort":
            self.score += 1

        self.result()


game = Game()
game.start()
