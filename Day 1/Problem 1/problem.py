def calculateNumber(text):
    """This function calculates the sum of the first digit and last digit in a given string.

    Args:
        text (str): The text string containing first and last digit.

    >>> calculateNumber("1abc2")
    12
    >>> calculateNumber("pqr3stu8vwx")
    38
    >>> calculateNumber("a1b2c3d4e5f")
    15
    >>> calculateNumber("treb7uchet")
    77
    >>> calculateNumber("aaaa")
    0
    """
    first = None
    last = None
    for character in text:
        if str.isdigit(character):
            first = character
            break
    for i in range(len(text) - 1,-1,-1):
        if str.isdigit(text[i]):
            last = text[i]
            break
    if first == None or last == None:
        return 0
    return int(first+last)


if __name__ == "__main__":
    sum = 0
    with open('input.txt','r') as inputFile:
        inputFileLines = inputFile.readlines()
        for inputFileLine in inputFileLines:
            sum = sum + calculateNumber(inputFileLine)

    print(sum)