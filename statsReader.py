import pandas as pd
import numpy as np

# TODO: Timeline? TODO: differentiate quarter change: when T+(previous) > T+(current), that means there's a quarter 
#  change. To double check, if time difference is bigger than 15 min, quarter change 

MAX_ARRAY_ROWS = 6
# NEVER FORGET OUR BEST PLAYER: MR. PLACEHOLDER, HIS JERSEY NUMBER IS XX
headingResult = np.empty([10, 3], 'U50')
# expected structure: [STRING, Time, Time]
# note: https://stackoverflow.com/questions/55377213/numpy-taking-only-first-character-of-string
# type str only takes the first character of string
# use U + length instead
selfScoreResult = np.empty([MAX_ARRAY_ROWS, 5], 'U50')
opponentScoreResult = np.empty([MAX_ARRAY_ROWS, 5], 'U50')
# expected structure: [Main, Assist1, Assist2, Time Happened, Quarter T+]
selfSaveResult = np.empty([MAX_ARRAY_ROWS, 3], 'U50')
opponentSaveResult = np.empty([MAX_ARRAY_ROWS, 3], 'U50')
# expected structure: [Goalie, Time Happened, Quarter T+]
selfGroundballResult = np.empty([MAX_ARRAY_ROWS, 3], 'U50')
opponentGroundballResult = np.empty([MAX_ARRAY_ROWS, 3], 'U50')
# expected structure: [Who Picked-up, Time Happened, Quarter T+]
selfTurnoverResult = np.empty([MAX_ARRAY_ROWS, 4], 'U50')
opponentTurnoverResult = np.empty([MAX_ARRAY_ROWS, 4], 'U50')
# expected structure：[Who Caused, Who Dropped, Time Happened, Quarter T+]
selfPenaltyResult = np.empty([MAX_ARRAY_ROWS, 5], 'U50')
opponentPenaltyResult = np.empty([MAX_ARRAY_ROWS, 5], 'U50')
# expected structure: [Main, Type, Length, Time Happened, Quarter T+]
headingList = []  # storing info about game heading
selfList = []  # storing info about your team
opponentList = []  # storing info about the opponent team
selfScoreList = []
opponentScoreList = []
selfSaveList = []
opponentSaveList = []
selfGroundballList = []
opponentGroundballList = []
selfTurnoverList = []
opponentTurnoverList = []
selfPenaltyList = []
opponentPenaltyList = []

with open('record.txt') as f:
    lines = [line.rstrip() for line in f]  # storing everything
f.close()

for self in lines:
    if self[0] != '#' and self[0] != '*':
        selfList.append(self)
    elif self[0] != '*':
        opponentList.append(self.replace('#', ''))


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
            print("Current line is blank")
        i += 1
    headingList.pop(0)
    headingList.pop(0)
    # i, x = 0, 0  # reset var i, x

    for x in range(len(headingList)):
        split = headingList[x].split(',')
        headingResult[x][0] = split[0]
        headingResult[x][1] = split[1]
        headingResult[x][2] = split[2]


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
            print("Current line is blank")
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

        selfScoreResult[x][0] = str(numbers[0]) + str(numbers[1])
        selfScoreResult[x][1] = str(numbers[2]) + str(numbers[3])
        selfScoreResult[x][2] = str(numbers[4]) + str(numbers[5])
        selfScoreResult[x][3] = split[1]
        selfScoreResult[x][4] = split[2]


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
            print("Current line is blank")
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

        opponentScoreResult[x][0] = str(numbers[0]) + str(numbers[1])
        opponentScoreResult[x][1] = str(numbers[2]) + str(numbers[3])
        opponentScoreResult[x][2] = str(numbers[4]) + str(numbers[5])
        opponentScoreResult[x][3] = split[1]
        opponentScoreResult[x][4] = split[2]


def get_self_save():
    linesLen = len(selfList)
    i = 0
    for x in range(linesLen):
        current = selfList[i]
        try:
            if current[0] == 'g':
                removed = selfList.pop(i)
                removed = removed[1:]
                selfSaveList.append(removed)
                i -= 1
        except IndexError:
            print("Current line is blank")
        i += 1
    # print(selfScoreList)
    # i, x = 0, 0  # reset var i, x
    for x in range(len(selfSaveList)):
        split = selfSaveList[x].split(',')
        selfSaveResult[x][0] = split[0]
        selfSaveResult[x][1] = split[1]
        selfSaveResult[x][2] = split[2]


def get_opponent_save():
    linesLen = len(opponentList)
    i = 0
    for x in range(linesLen):
        current = opponentList[i]
        try:
            if current[0] == 'g':
                removed = opponentList.pop(i)
                removed = removed[1:]
                opponentSaveList.append(removed)
                i -= 1
        except IndexError:
            print("Current line is blank")
        i += 1
    # print(opponentScoreList)
    # i, x = 0, 0  # reset var i, x
    for x in range(len(opponentSaveList)):
        split = opponentSaveList[x].split(',')
        opponentSaveResult[x][0] = split[0]
        opponentSaveResult[x][1] = split[1]
        opponentSaveResult[x][2] = split[2]


def get_self_groundball():
    linesLen = len(selfList)
    i = 0
    for x in range(linesLen):
        current = selfList[i]
        try:
            if current[0] == 'b':
                removed = selfList.pop(i)
                removed = removed[1:]
                selfGroundballList.append(removed)
                i -= 1
        except IndexError:
            print("Current line is blank")
        i += 1
    # print(selfScoreList)
    # i, x = 0, 0  # reset var i, x
    for x in range(len(selfGroundballList)):
        split = selfGroundballList[x].split(',')
        if split[0] == '':
            split[0] = "xx"
        selfGroundballResult[x][0] = split[0]
        selfGroundballResult[x][1] = split[1]
        selfGroundballResult[x][2] = split[2]


def get_opponent_groundball():
    linesLen = len(opponentList)
    i = 0
    for x in range(linesLen):
        current = opponentList[i]
        try:
            if current[0] == 'b':
                removed = opponentList.pop(i)
                removed = removed[1:]
                opponentGroundballList.append(removed)
                i -= 1
        except IndexError:
            print("Current line is blank")
        i += 1
    # print(opponentScoreList)
    # i, x = 0, 0  # reset var i, x
    for x in range(len(opponentGroundballList)):
        split = opponentGroundballList[x].split(',')
        if split[0] == '':
            split[0] = "xx"
        opponentGroundballResult[x][0] = split[0]
        opponentGroundballResult[x][1] = split[1]
        opponentGroundballResult[x][2] = split[2]


def get_self_penalty():
    linesLen = len(selfList)
    i = 0
    for x in range(linesLen):
        current = selfList[i]
        try:
            if current[0] == 'p':
                removed = selfList.pop(i)
                removed = removed[1:]
                selfPenaltyList.append(removed)
                i -= 1
        except IndexError:
            print("Current line is blank")
        i += 1
    # print(selfScoreList)
    # i, x = 0, 0  # reset var i, x
    # expected structure: [Main, Type, Length, Time Happened, Quarter T+]
    # input: p02t2
    for x in range(len(selfPenaltyList)):
        split = selfPenaltyList[x].split(',')
        selfPenaltyResult[x][0] = split[0][0] + split[0][1]
        selfPenaltyResult[x][1] = split[0][2]
        selfPenaltyResult[x][2] = split[0][3]
        selfPenaltyResult[x][3] = split[1]
        selfPenaltyResult[x][4] = split[2]


def get_opponent_penalty():
    linesLen = len(opponentList)
    i = 0
    for x in range(linesLen):
        current = opponentList[i]
        try:
            if current[0] == 'p':
                removed = opponentList.pop(i)
                removed = removed[1:]
                opponentPenaltyList.append(removed)
                i -= 1
        except IndexError:
            print("Current line is blank")
        i += 1
    # print(opponentScoreList)
    # i, x = 0, 0  # reset var i, x
    # expected structure: [Main, Type, Length, Time Happened, Quarter T+]
    # input: p02t2
    for x in range(len(opponentPenaltyList)):
        split = opponentPenaltyList[x].split(',')
        opponentPenaltyResult[x][0] = split[0][0] + split[0][1]
        opponentPenaltyResult[x][1] = split[0][2]
        opponentPenaltyResult[x][2] = split[0][3]
        opponentPenaltyResult[x][3] = split[1]
        opponentPenaltyResult[x][4] = split[2]
        

def get_self_turnover():
    linesLen = len(selfList)
    i = 0
    for x in range(linesLen):
        current = selfList[i]
        try:
            if current[0] == 't':
                removed = selfList.pop(i)
                removed = removed[1:]
                selfTurnoverList.append(removed)
                i -= 1
        except IndexError:
            print("Current line is blank")
        i += 1
    # print(selfTurnoverList)
    # i, x = 0, 0  # reset var i, x

    for x in range(len(selfTurnoverList)):
        numbers = []
        split = selfTurnoverList[x].split(',')

        while (len(split[0]) <= 4):
            split[0] = str(split[0]) + "xx"

        for i in range(len(split[0])):
            numbers.append(split[0][i])
        # expected structure：[Who Caused, Who Dropped, Time Happened, Quarter T+]
        selfTurnoverResult[x][0] = str(numbers[0]) + str(numbers[1])
        selfTurnoverResult[x][1] = str(numbers[2]) + str(numbers[3])
        selfTurnoverResult[x][2] = split[1]
        selfTurnoverResult[x][3] = split[2]


def get_opponent_turnover():
    linesLen = len(opponentList)
    i = 0
    for x in range(linesLen):
        current = opponentList[i]
        try:
            if current[0] == 't':
                removed = opponentList.pop(i)
                removed = removed[1:]
                opponentTurnoverList.append(removed)
                i -= 1
        except IndexError:
            print("Current line is blank")
        i += 1
    # print(opponentTurnoverList)
    # i, x = 0, 0  # reset var i, x

    for x in range(len(opponentTurnoverList)):
        numbers = []
        split = opponentTurnoverList[x].split(',')

        while (len(split[0]) <= 4):
            split[0] = str(split[0]) + "xx"

        for i in range(len(split[0])):
            numbers.append(split[0][i])
        # expected structure：[Who Caused, Who Dropped, Time Happened, Quarter T+]
        opponentTurnoverResult[x][0] = str(numbers[0]) + str(numbers[1])
        opponentTurnoverResult[x][1] = str(numbers[2]) + str(numbers[3])
        opponentTurnoverResult[x][2] = split[1]
        opponentTurnoverResult[x][3] = split[2]
        
# Testing Area


get_heading()
print("HEADING")
print(headingResult)

get_self_score()
print("SELF SCORE")
print(selfScoreResult)

get_opponent_score()
print("OPPONENT SCORE")
print(opponentScoreResult)

get_self_save()
print("SELF SAVE")
print(selfSaveResult)

get_opponent_save()
print("OPPONENT SAVE")
print(opponentSaveResult)

get_self_groundball()
print("SELF GROUNDBALL")
print(selfGroundballResult)

get_opponent_groundball()
print("OPPONENT GROUNDBALL")
print(opponentGroundballResult)

get_self_penalty()
print("SELF PENALTY")
print(selfPenaltyResult)

get_opponent_penalty()
print("OPPONENT PENALTY")
print(opponentPenaltyResult)

get_self_turnover()
print("SELF TURNOVER")
print(selfTurnoverResult)

get_opponent_turnover()
print("OPPONENT TURNOVER")
print(opponentTurnoverResult)