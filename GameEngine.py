#Name: Kshitij Patil & Shreyak Godala
#Date: 12/04/2023
#Description: Implementing the game engine file

import random
from FieldInhabitant import FieldInhabitant 
from Captain import Captain
from Veggie import Veggie
from Rabbit import Rabbit

class GameEngine:
    NUMBEROFVEGGIES = 30
    NUMBEROFRABBITS = 5
    HIGHSCOREFILE = "highscore.data"

    def __init__(self):
        self.field = []  # Represents the field as a 2D List
        self.rabbits = []  # List to store Rabbit objects
        self.captain = None  # Variable to store the Captain object
        self.possible_veggies = []  # List to store possible vegetable objects
        self.score = 0  # Variable to store the score

    def initVeggies(self):
        # Prompt user for veggie file
        while True:
            filename = input("Enter the veggie file name: ")
            try:
                with open(filename, 'r') as file:
                    lines = file.readlines()
                    # Initialize the field
                    self.field = [[None for _ in range(int(lines[0]))] for _ in range(int(lines[1]))]
                    # Populate possible_veggies list
                    for line in lines[2:]:
                        veggie_info = line.strip().split(',')
                        symbol, name, points = veggie_info[0], veggie_info[1], int(veggie_info[2])
                        self.possible_veggies.append(Veggie(symbol, name, points))
                    break
            except FileNotFoundError:
                print("File not found. Enter a valid file name.")

        # Place NUMBEROFVEGGIES randomly in the field
        for _ in range(self.NUMBEROFVEGGIES):
            while True:
                x, y = random.randint(0, len(self.field) - 1), random.randint(0, len(self.field[0]) - 1)
                if self.field[x][y] is None:
                    veggie = random.choice(self.possible_veggies)
                    self.field[x][y] = veggie
                    break

    def initCaptain(self):
        # Initialize Captain object randomly
        while True:
            x, y = random.randint(0, len(self.field) - 1), random.randint(0, len(self.field[0]) - 1)
            if self.field[x][y] is None:
                self.captain = Captain(x, y) 
                self.field[x][y] = self.captain
                break

    def initRabbits(self):
        for _ in range(self.NUMBEROFRABBITS):
            while True:
                x, y = random.randint(0, len(self.field) - 1), random.randint(0, len(self.field[0]) - 1)
                if self.field[x][y] is None:
                    rabbit = Rabbit(x, y) 
                    self.field[x][y] = rabbit
                    self.rabbits.append(rabbit)
                    break

    def initializeGame(self):
        self.initVeggies()
        self.initCaptain()
        self.initRabbits()

    def remainingVeggies(self):
        count = sum(row.count(None) for row in self.field)
        return count

    def intro(self):
        print("Welcome to the Vegetable Harvesting Game!")
        print("The goal of the game is to collect as many vegetables as possible while avoiding the rabbits.")
        print("List of vegetables, their symbols, names, and point values:")
        for veggie in self.possible_veggies:
            print(veggie)

        print(f"Captain's symbol: {self.captain.getSymbol()}")
        print(f"Rabbit's symbol: {self.rabbits[0].getSymbol()}") 

    def printField(self):
        print("Field Contents:")
        print("-" * (len(self.field[0]) * 4 + 3))
        for row in self.field:
            print("|", end=" ")
            for col in row:
                print(col.getSymbol() if col else " ", end=" | ")
            print("\n" + "-" * (len(row) * 4 + 3))

    def getScore(self):
        return self.score

    def moveRabbits(self):
        for rabbit in self.rabbits:
            x = rabbit.get_x()
            y = rabbit.get_y()

            # Generate a random direction to move
            move_x = random.randint(-1, 1)
            move_y = random.randint(-1, 1)

            # Check if the move is within the field and available
            new_x = x + move_x
            new_y = y + move_y

            if 0 <= new_x < len(self.field) and 0 <= new_y < len(self.field[0]):
                if self.field[new_x][new_y] is None:
                    # Move the rabbit and update its location
                    self.field[new_x][new_y] = rabbit
                    self.field[x][y] = None
                    rabbit.set_x(new_x)
                    rabbit.set_y(new_y)
                elif isinstance(self.field[new_x][new_y], Veggie):
                    # If the rabbit finds a veggie, remove it and update rabbit's location
                    veggie = self.field[new_x][new_y]
                    self.field[new_x][new_y] = rabbit
                    self.field[x][y] = None
                    rabbit.set_x(new_x)
                    rabbit.set_y(new_y)
                    self.possible_veggies.remove(veggie)

    #Please implement these functions and check if everything works properly

    # def moveCptVertical()

    # def moveCptHorizontal()

    # def moveCaptain() 

    def gameOver(self):
        print("Game Over!")
        harvested_veggies = [veggie.getName() for row in self.field for veggie in row if isinstance(veggie, Veggie)]
        if not harvested_veggies:
            print("Captain didn't harvest any vegetables.")
        else:
            print("The Captain harvested the following vegetables:")
            for veggie in harvested_veggies:
                print(f"- {veggie}")

        print(f"Player's score: {self.score}")

    # def highScore()



