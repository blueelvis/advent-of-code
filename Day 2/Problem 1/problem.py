import re
def getGameId(text : str) -> int:
    """For a given string from the input, returns the ID of the game.

    Example input -
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green" --> Returns 1
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue" --> Returns 2
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red" --> Returns 3
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red" --> Returns 4
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green" --> Returns 5
    Args:
        text (str): The line containing the Game ID

    Returns:
        int: The integer value of the Game ID.

    >>> getGameId("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    1
    >>> getGameId("Game 30: 1 green, 1 red, 5 blue; 13 blue, 4 green, 2 red; 10 green, 11 blue; 9 green, 2 red, 12 blue")
    30
    """
    return int(text.split(":")[0].split(" ")[1])

def isGamePossible(text: str) -> bool:
    """Determines if the game is possible for the given number of rounds and cubes drawn.

    Args:
        text (str): The string containing the game along with the rounds.

    Returns:
        bool: Returns True if the game is possible, False otherwise.

    >>> isGamePossible("Game 55: 6 green, 11 blue, 12 red; 10 blue, 6 red, 13 green; 7 green, 9 blue; 10 green, 20 red, 7 blue; 9 green, 14 red, 8 blue; 14 green, 15 red")
    False
    >>> isGamePossible("Game 2: 1 blue, 11 red, 1 green; 3 blue, 2 red, 4 green; 11 red, 2 green, 2 blue; 13 green, 5 red, 1 blue; 4 green, 8 red, 3 blue")
    True
    >>> isGamePossible("Game 1: 4 green, 2 blue; 1 red, 1 blue, 4 green; 3 green, 4 blue, 1 red; 7 green, 2 blue, 4 red; 3 red, 7 green; 3 red, 3 green")
    True
    """

    maxRedCubes = 12
    maxGreenCubes = 13
    maxBlueCubes = 14
    game = text.split(":")[1]
    rounds = game.split(";")
    for round in rounds:
        for cubes in round.split(','):
            temp = cubes.replace(" ","")
            if "blue" in temp and int(re.findall(r'\d+', temp)[0]) > maxBlueCubes:
                return False
            if "green" in temp and int(re.findall(r'\d+', temp)[0]) > maxGreenCubes:
                return False
            if "red" in temp and int(re.findall(r'\d+', temp)[0]) > maxRedCubes:
                return False
    return True



if __name__ == "__main__":
    sum = 0
    with open('input.txt','r') as inputFile:
        inputFileLines = inputFile.readlines()
        for inputFileLine in inputFileLines:
            if isGamePossible(inputFileLine):
                sum = sum + getGameId(inputFileLine)

    print(sum)