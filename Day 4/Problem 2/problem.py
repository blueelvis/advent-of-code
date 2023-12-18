def getCountOfWinningNumbers(text: str) -> int:
    """Returns the number of winning numbers in the card game as per README.md

    Args:
        text (str): The string containing the game with the scratch card numbers.

    Returns:
        int: Returns the number of winning numbers.

    >>> getCountOfWinningNumbers("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53")
    4
    >>> getCountOfWinningNumbers("Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19")
    2
    >>> getCountOfWinningNumbers("Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36")
    0
    >>> getCountOfWinningNumbers("Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1")
    2
    """

    points = 0
    numbers = text.split(":")[1]
    #numbers = text
    winningNumbers = list(map(int, list(filter(None,numbers.split("|")[0].split(" ")))))
    ourNumbers = list(map(int, list(filter(None,numbers.split("|")[1].split(" ")))))
    for ourNumber in ourNumbers:
        if ourNumber in winningNumbers:
            points += 1
    return points



if __name__ == "__main__":
    sum = 0
    cardWins = dict()
    copies = dict()

    with open('input.txt','r') as inputFile:
        inputFileLines = inputFile.readlines()
        for i in range(1, len(inputFileLines)+1):
            cardWins[i] = getCountOfWinningNumbers(inputFileLines[i-1])
            copies[i] = 1
        #breakpoint()
        for card in copies.keys():
            wins = cardWins[card]
            for i in range(card+1, card+wins+1):
                copies[i] += copies[card]

        for key in copies.keys():
            sum += copies[key]

    print(sum)