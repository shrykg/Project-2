#Name: Kshitij Patil & Shreyak Godala
#Date: 12/04/2023
#Description: Implementing the game engine file

import random
import os
import pickle
from FieldInhabitant import FieldInhabitant 
from Captain import Captain
from Veggie import Veggie
from Rabbit import Rabbit

class GameEngine:
    NUMBEROFVEGGIES = 30
    NUMBEROFRABBITS = 5
    HIGHSCOREFILE = "highscore.data"

    def __init__(self):
        self.__field = []  # Represents the field as a 2D List
        self.__rabbits = []  # List to store Rabbit objects
        self.__captain = None  # Variable to store the Captain object
        self.__possible_veggies = []  # List to store possible vegetable objects
        self.__score = 0  # Variable to store the score

    def initVeggies(self):
        # Prompt user for veggie file
        while True:
            filename = input("Enter the veggie file name: ")
            try:
                with open(filename, 'r') as file:
                    lines = file.readlines()
                    # Initialize the field
                    self.__field = [[None for _ in range(int(lines[0]))] for _ in range(int(lines[1]))]
                    # Populate possible_veggies list
                    for line in lines[2:]:
                        veggie_info = line.strip().split(',')
                        symbol, name, points = veggie_info[0], veggie_info[1], int(veggie_info[2])
                        self.__possible_veggies.append(Veggie(symbol, name, points))
                    break
            except FileNotFoundError:
                print("File not found. Enter a valid file name.")

        # Place NUMBEROFVEGGIES randomly in the field
        for _ in range(self.NUMBEROFVEGGIES):
            while True:
                x, y = random.randint(0, len(self.__field) - 1), random.randint(0, len(self.__field[0]) - 1)
                if self.__field[x][y] is None:
                    veggie = random.choice(self.__possible_veggies)
                    self.__field[x][y] = veggie
                    break

    def initCaptain(self):
        # Initialize Captain object randomly
        while True:
            x, y = random.randint(0, len(self.__field) - 1), random.randint(0, len(self.__field[0]) - 1)
            if self.__field[x][y] is None:
                self.__captain = Captain(x, y)
                self.__field[x][y] = self.__captain
                break

    def initRabbits(self):
        for _ in range(self.NUMBEROFRABBITS):
            while True:
                x, y = random.randint(0, len(self.__field) - 1), random.randint(0, len(self.__field[0]) - 1)
                if self.__field[x][y] is None:
                    rabbit = Rabbit(x, y) 
                    self.__field[x][y] = rabbit
                    self.__rabbits.append(rabbit)
                    break

    def initializeGame(self):
        self.initVeggies()
        self.initCaptain()
        self.initRabbits()

    def remainingVeggies(self):
        count = sum(row.count(None) for row in self.__field)
        return count

    def intro(self):
        print("Welcome to the Vegetable Harvesting Game!")
        print("The goal of the game is to collect as many vegetables as possible while avoiding the rabbits.")
        print("List of vegetables, their symbols, names, and point values:")
        for veggie in self.__possible_veggies:
            print(veggie)

        print(f"Captain's symbol: {self.__captain.getSymbol()}")
        print(f"Rabbit's symbol: {self.__rabbits[0].getSymbol()}")

    def printField(self):
        print("Field Contents:")
        print("-" * (len(self.__field[0]) * 4 + 3))
        for row in self.__field:
            print("|", end=" ")
            for col in row:
                print(col.getSymbol() if col else " ", end=" | ")
            print("\n" + "-" * (len(row) * 4 + 3))

    def getScore(self):
        return self.__score

    def moveRabbits(self):
        for rabbit in self.__rabbits:
            x = rabbit.get_x()
            y = rabbit.get_y()

            # Generate a random direction to move
            move_x = random.randint(-1, 1)
            move_y = random.randint(-1, 1)

            # Check if the move is within the field and available
            new_x = x + move_x
            new_y = y + move_y

            if 0 <= new_x < len(self.__field) and 0 <= new_y < len(self.__field[0]):
                if self.__field[new_x][new_y] is None:
                    # Move the rabbit and update its location
                    self.__field[new_x][new_y] = rabbit
                    self.__field[x][y] = None
                    rabbit.set_x(new_x)
                    rabbit.set_y(new_y)
                elif isinstance(self.__field[new_x][new_y], Veggie):
                    # If the rabbit finds a veggie, remove it and update rabbit's location
                    veggie = self.__field[new_x][new_y]
                    self.__field[new_x][new_y] = rabbit
                    self.__field[x][y] = None
                    rabbit.set_x(new_x)
                    rabbit.set_y(new_y)
                    self.__possible_veggies.remove(veggie)



    def moveCptVertical(self, verticalMovement):
        # get current position of captain
        currentX = self.__captain.get_x()
        currentY = self.__captain.get_y()
        newX = currentX
        newY = currentY
        if verticalMovement.lower() == 'w':
            newY -= 1
        elif verticalMovement.lower() == 's':
            newY += 1

        # make sure movement is within the boundary of field
        if 0 <= newX < len(self.__field) and 0 <= newY < len(self.__field[0]):
            if self.__field[newX][newY] is None:
                # case where captain moves to empty space in field
                self.__field[currentX][currentY] = None
                self.__field[newX][newY] = self.__captain
                self.__captain.set_x(newX)
                self.__captain.set_y(newY)

            elif isinstance(self.__field[newX][newY], Veggie):
                # case where there is a veggie in new position
                self.__captain.set_x(newX)
                self.__captain.set_y(newY)
                veggie = self.__field[newX][newY]
                print(f'Yummy! A delicious {veggie.getName()}')
                self.__possible_veggies.remove(veggie)
                self.__captain.addVeggie(veggie)
                self.__score += veggie.getPoints()
                self.__field[newX][newY] = self.__captain

            elif isinstance(self.__field[newX][newY], Rabbit):
                # case where there is rabbit so don't move and inform user about it
                print("Watch out for the rabbits! Don't step on them.")

    def moveCptHorizontal(self, horizontalMovement):
        # get current position of captain
        currentX = self.__captain.get_x()
        currentY = self.__captain.get_y()
        newX = currentX
        newY = currentY
        # set new position based on movement
        if horizontalMovement.lower() == 'a':
            newX -= 1
        elif horizontalMovement.lower() == 'd':
            newX += 1

        # make sure movement is within the boundary of field
        if 0 <= newX < len(self.__field) and 0 <= newY < len(self.__field[0]):
            if self.__field[newX][newY] is None:
                # case where captain moves to empty space in field
                self.__field[currentX][currentY] = None
                self.__field[newX][newY] = self.__captain
                self.__captain.set_x(newX)
                self.__captain.set_y(newY)

            elif isinstance(self.__field[newX][newY], Veggie):
                # case where there is a veggie in new position
                self.__captain.set_x(newX)
                self.__captain.set_y(newY)
                veggie = self.__field[newX][newY]
                print(f'Yummy! A delicious {veggie.getName()}')
                self.__possible_veggies.remove(veggie)
                self.__captain.addVeggie(veggie)
                self.__score += veggie.getPoints()
                self.__field[newX][newY] = self.__captain

            elif isinstance(self.__field[newX][newY], Rabbit):
                # case where there is rabbit so don't move and inform user about it
                print("Watch out for the rabbits! Don't step on them.")

    def moveCaptain(self):

        direction = input('Would you like to move up(W), down(S), left(A), or right(D)').lower()

        if direction == 'w' or 's': # if direction is up or down call moveCptVertical
            self.moveCptVertical(direction)
        elif direction == 'a' or 'd': # # if direction is left or right call moveCptHorizontal
            self.moveCptHorizontal(direction)
        else:
            print(f'{direction} is not a valid option')


    def gameOver(self):
        # game over function after all veggies are over
        print("Game Over!")
        harvested_veggies = [veggie.getName() for row in self.__field for veggie in row if isinstance(veggie, Veggie)]
        if not harvested_veggies:
            print("Captain didn't harvest any vegetables.")
        else:
            print("The Captain harvested the following vegetables:")
            for veggie in harvested_veggies:
                print(f"- {veggie}")

        print(f"Player's score: {self.__score}")

    def highScore(self):
        # Declare an empty List to store Tuples representing player initials and their score
        high_scores = []
        # Check if the highscore.data file exists
        if os.path.exists(self.HIGHSCOREFILE):
            # Open the file for binary reading
            with open(self.HIGHSCOREFILE, 'rb') as file:
                # Unpickle the file into the List of high scores
                high_scores = pickle.load(file)

        # Prompt the user for their initials and extract the first 3 characters
        player_initials = input("Please enter your three initials to go on the scoreboard: ")[:3]

        # Create a Tuple with the player’s initials and score
        player_score = (player_initials, self.__score)

        # Append the player's initials and current score to the list
        high_scores.append(player_score)

        # Sort the list in descending order of scores
        high_scores.sort(key=lambda x: x[1], reverse=True)

        # Output all of the high scores
        print("HIGH SCORES")
        print("Name\tScore")
        for rank, (initials, score) in enumerate(high_scores, start=1):
            print(f"{initials}\t\t{score}")

        # Open the highscore.data file for binary writing
        with open(self.HIGHSCOREFILE, 'wb') as file:
            # Pickle the List of high scores to the file
            pickle.dump(high_scores, file)


