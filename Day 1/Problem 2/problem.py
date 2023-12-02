import re
patterns = {
    "o(?=ne)" : "1",
    "t(?=wo)" : "2",
    "t(?=hree)" : "3",
    "f(?=our)" : "4",
    "f(?=ive)" : "5",
    "s(?=ix)" : "6",
    "s(?=even)" : "7",
    "e(?=ight)" : "8",
    "n(?=ine)": "9"
}

def checkAndReplaceLookAhead(text: str):
    """This function does a REGEX lookahead for the digits worded as numbers and then returns true or false.

    Args:
        text (str): The string to check

    >>> checkAndReplaceLookAhead("twonetwo9")
    '2129'
    >>> checkAndReplaceLookAhead("xtwone3four")
    '2134'
    >>> checkAndReplaceLookAhead("4nineeightseven2")
    '49872'
    """
    temp = [""]*len(text)
    for i in range(0, len(text)):
        if text[i].isdigit():
            temp[i] = text[i]
    for pattern in patterns.keys():
        it = re.finditer(pattern=pattern, string=text)
        for i in it:
            position = i.span()
            temp[position[0]] = patterns[pattern]
    return "".join(temp)

if __name__ == "__main__":
    sum = 0
    with open('input.txt','r') as inputFile:
        inputFileLines = inputFile.readlines()
        for inputFileLine in inputFileLines:
            transformedString = checkAndReplaceLookAhead(inputFileLine)
            sum = sum + (int(transformedString[0] + transformedString[-1]))
    print(sum)