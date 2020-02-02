import pandas as pd
import numpy as np

heading = np.empty([10, 3], 'U50')
# expected structure: [STRING, Time, Time]
# note: https://stackoverflow.com/questions/55377213/numpy-taking-only-first-character-of-string
# type str only takes the first character of string
# use U + length instead
selfScore = np.empty([100, 5], 'U50')
# expected structure: [Main, Assist1, Assist2, Time Happened, Quarter T+]
opponentScore = np.empty([100, 5], 'U50')
# expected structure: [Main, Assist1, Assist2, Time Happened, Quarter T+]


headingList = []  # storing info about game heading
selfList = []  # storing info about your team
opponentList = []  # storing info about the opponent team
selfScoreList = []
opponentScoreList = []

with open('record.txt') as f:
    lines = [line.rstrip() for line in f]  # storing everything
    print(lines)
f.close()

for self in lines:
    if self[0] != '#' and self[0] != '*':
        selfList.append(self)
    elif self[0] != '*':
        opponentList.append(self.replace('#', ''))

print(selfList)
print(opponentList)


def get_heading():
    linesLen = len(lines)
    i = 0
    for x in range(linesLen):
        current = lines[i]
        try:
            if current[0] == 'i':
                removed = lines.pop(i)
                removed = removed[1:]
                headingList.append(removed)
                i -= 1
        except IndexError:
            print("current line is blank")
        i += 1
    headingList.pop(0)
    headingList.pop(0)
    print(headingList)
    # i, x = 0, 0  # reset var i, x

    for x in range(len(headingList)):
        split = headingList[x].split(',')
        print(split)
        heading[x][0] = split[0]
        heading[x][1] = split[1]
        heading[x][2] = split[2]

    print(heading)


def get_self_score():
    linesLen = len(selfList)
    i = 0
    for x in range(linesLen):
        current = selfList[i]
        try:
            if current[0] == 'a':
                removed = selfList.pop(i)
                removed = removed[1:]
                selfScoreList.append(removed)
                i -= 1
        except IndexError:
            print("current line is blank")
        i += 1
    # print(selfScoreList)
    # i, x = 0, 0  # reset var i, x

    for x in range(len(selfScoreList)):
        numbers = []
        split = selfScoreList[x].split(',')

        while (len(split[0]) <= 6):
            split[0] = str(split[0]) + "xx"

        for i in range(len(split[0])):
            numbers.append(split[0][i])

        selfScore[x][0] = str(numbers[0]) + str(numbers[1])
        selfScore[x][1] = str(numbers[2]) + str(numbers[3])
        selfScore[x][2] = str(numbers[4]) + str(numbers[5])
        selfScore[x][3] = split[1]
        selfScore[x][4] = split[2]

    print(selfScore)


def get_opponent_score():
    linesLen = len(opponentList)
    i = 0
    for x in range(linesLen):
        current = opponentList[i]
        try:
            if current[0] == 'a':
                removed = opponentList.pop(i)
                removed = removed[1:]
                opponentScoreList.append(removed)
                i -= 1
        except IndexError:
            print("current line is blank")
        i += 1
    # print(opponentScoreList)
    # i, x = 0, 0  # reset var i, x

    for x in range(len(opponentScoreList)):
        numbers = []
        split = opponentScoreList[x].split(',')

        while len(split[0]) <= 6:
            split[0] = str(split[0]) + "xx"

        for i in range(len(split[0])):
            numbers.append(split[0][i])

        opponentScore[x][0] = str(numbers[0]) + str(numbers[1])
        opponentScore[x][1] = str(numbers[2]) + str(numbers[3])
        opponentScore[x][2] = str(numbers[4]) + str(numbers[5])
        opponentScore[x][3] = split[1]
        opponentScore[x][4] = split[2]

    print(opponentScore)


# get_heading()
get_self_score()
get_opponent_score()
