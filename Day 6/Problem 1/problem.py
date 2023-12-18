def checkIfWinsRace(startTime: int, totalTime: int, winningDistance: int):

    carRunTime = totalTime - startTime
    speed = startTime
    if carRunTime * speed > winningDistance:
        return True
    return False


if __name__ == "__main__":
    product = 1
    with open('input.txt','r') as inputFile:
        inputFileLines = inputFile.readlines()

        # Do some parsing.
        time = inputFileLines[0].split(":")[1].replace("\n","").split(" ")
        winningDistance = inputFileLines[1].split(":")[1].replace("\n","").split(" ")
        time.pop(0)
        winningDistance.pop(0)

        for race in range(0, len(time)):
            raceWinningDistance = int(winningDistance[race])
            raceTotalTime = int(time[race])
            waysToWin = 0
            for i in range(1, raceTotalTime):
                if checkIfWinsRace(startTime=i, totalTime=raceTotalTime, winningDistance=raceWinningDistance):
                    waysToWin += 1
            product = product * waysToWin

        print(product)