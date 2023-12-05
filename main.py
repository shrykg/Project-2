from GameEngine import GameEngine

def main():
    gameEngine = GameEngine()
    gameEngine.initializeGame()
    gameEngine.intro()
    veggiesRemaining = gameEngine.remainingVeggies()

    while veggiesRemaining > 0:
        print(f'{veggiesRemaining} veggies remaining. Current score: {gameEngine.getScore()}')
        gameEngine.printField()
        gameEngine.moveRabbits()
        gameEngine.moveCaptain()
        veggiesRemaining = gameEngine.remainingVeggies()

    gameEngine.gameOver()
    gameEngine.highScore()

main()