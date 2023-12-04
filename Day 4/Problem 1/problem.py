def getScratchCardPoints(text: str) -> int:
    """Returns the points of a scratch card as per the game rules defined in README.txt

    Args:
        text (str): The string containing the game with the scratch card numbers.

    Returns:
        int: Returns the points of the scratch card.

    >>> getScratchCardPoints("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53")
    8
    >>> getScratchCardPoints("Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19")
    2
    >>> getScratchCardPoints("Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11")
    0
    """

    points = 0
    numbers = text.split(":")[1]
    winningNumbers = list(map(int, list(filter(None,numbers.split("|")[0].split(" ")))))
    ourNumbers = list(map(int, list(filter(None,numbers.split("|")[1].split(" ")))))
    for ourNumber in ourNumbers:
        if ourNumber in winningNumbers:
            if points == 0:
                points += 1
            else:
                points = points * 2
    return points



if __name__ == "__main__":
    sum = 0
    with open('input.txt','r') as inputFile:
        inputFileLines = inputFile.readlines()
        for inputFileLine in inputFileLines:
            sum = sum + getScratchCardPoints(inputFileLine)

    print(sum)