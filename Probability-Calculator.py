import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = [key for key, val in kwargs.items() for i in range(val)]

    def draw(self, numberOfBalls):

        if numberOfBalls > len(self.contents):
            numberOfBalls = len(self.contents)

        ballsDrawndraw = []
        while numberOfBalls > 0:
            x = self.contents.pop(random.randint(0, len(self.contents)-1))
            ballsDrawndraw.append(x)
            numberOfBalls -= 1
        return ballsDrawndraw


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    experimentsDone = 0
    numberOfPositives = 0

    while experimentsDone < num_experiments:
        copyOfHat = copy.deepcopy(hat)
        balls = copyOfHat.draw(num_balls_drawn)
        ballsdrawn = dict()
        for ball in balls:
            ballsdrawn[ball] = ballsdrawn.get(ball, 0) + 1
        print(ballsdrawn)
        num = 0
        for k, v in expected_balls.items():
            if v <= ballsdrawn.get(k, 0):
                num += 1
        if num == len(expected_balls):
            numberOfPositives += 1
        experimentsDone += 1
    probability = numberOfPositives / experimentsDone
    return probability

hat = Hat(black=6, red=4, green=3)
print(hat.contents)


probability = experiment(
    hat=hat,
    expected_balls={"red": 1,
                    "black": 2},
    num_balls_drawn=4,
    num_experiments=10)
print("Probability:", probability)
