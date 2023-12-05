#Name: Shreyak Godala
#Date: 12/04/2023
#Description: Implemention of the main file for running the game
from GameEngine import GameEngine

def main():
    # initialize the game
    gameEngine = GameEngine()
    gameEngine.initializeGame()
    gameEngine.intro()
    veggiesRemaining = gameEngine.remainingVeggies() #store remaining veggies in this variable

    while veggiesRemaining > 0:
        # perform these steps until the remaining veggies are greater than 0
        print(f'{veggiesRemaining} veggies remaining. Current score: {gameEngine.getScore()}')
        gameEngine.printField()
        gameEngine.moveRabbits()
        gameEngine.moveCaptain()
        veggiesRemaining = gameEngine.remainingVeggies()

    # Output game over and highscore functionality
    gameEngine.gameOver()
    gameEngine.highScore()

main()