import random as rnd

class GuessNumber:
    def __init__(self):
        self.computerNumber = rnd.randint(0, 100)
        self.guessCount = 0
        self.Guesser()

    def Guesser(self):
        while True:
            self.userNum = int(input("Guess the number: "))
            self.guessCount += 1
            if self.userNum > self.computerNumber:
                print("Lower number please")
            elif self.userNum < self.computerNumber:
                print("Higher number please")
            else:
                print(f"Congratulations! You guessed the correct number:{self.computerNumber} in {self.guessCount} attempts.")
                break

game = GuessNumber()
