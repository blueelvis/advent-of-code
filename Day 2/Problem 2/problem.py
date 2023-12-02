import re

def getCubePower(text: str) -> int:
    """Returns the multiplication of the lowest number cubes required to play the game.
        For example, for "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. If any color had even one fewer cube, the game would have been impossible. The power of the minimum set of cubes in game 1 is 48.

    Args:
        text (str): The string containing the game along with the rounds.

    Returns:
        int: Returns multiplication of the minimum number of cubes required to play the game.

    >>> getCubePower("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    48
    >>> getCubePower("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue")
    12
    >>> getCubePower("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red")
    630
    """

    minRedCubes = 0
    minGreenCubes = 0
    minBlueCubes = 0
    game = text.split(":")[1]
    rounds = game.split(";")
    for round in rounds:
        for cubes in round.split(','):
            temp = cubes.replace(" ","")
            numberOfCubes = int(re.findall(r'\d+', temp)[0])
            if "blue" in temp and numberOfCubes > minBlueCubes:
                minBlueCubes = numberOfCubes
            if "green" in temp and numberOfCubes > minGreenCubes:
                minGreenCubes = numberOfCubes
            if "red" in temp and numberOfCubes > minRedCubes:
                minRedCubes = numberOfCubes
    return minRedCubes * minBlueCubes * minGreenCubes



if __name__ == "__main__":
    sum = 0
    with open('input.txt','r') as inputFile:
        inputFileLines = inputFile.readlines()
        for inputFileLine in inputFileLines:
            sum = sum + getCubePower(inputFileLine)

    print(sum)