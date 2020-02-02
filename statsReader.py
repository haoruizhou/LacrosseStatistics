import openpyxl
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
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
homeScoreResult = np.empty([MAX_ARRAY_ROWS, 5], 'U50')
visitorScoreResult = np.empty([MAX_ARRAY_ROWS, 5], 'U50')
# expected structure: [Main, Assist1, Assist2, Time Happened, Quarter T+]
homeSaveResult = np.empty([MAX_ARRAY_ROWS, 3], 'U50')
visitorSaveResult = np.empty([MAX_ARRAY_ROWS, 3], 'U50')
# expected structure: [Goalie, Time Happened, Quarter T+]
homeGroundballResult = np.empty([MAX_ARRAY_ROWS, 3], 'U50')
visitorGroundballResult = np.empty([MAX_ARRAY_ROWS, 3], 'U50')
# expected structure: [Who Picked-up, Time Happened, Quarter T+]
homeTurnoverResult = np.empty([MAX_ARRAY_ROWS, 4], 'U50')
visitorTurnoverResult = np.empty([MAX_ARRAY_ROWS, 4], 'U50')
# expected structure：[Who Caused, Who Dropped, Time Happened, Quarter T+]
homePenaltyResult = np.empty([MAX_ARRAY_ROWS, 5], 'U50')
visitorPenaltyResult = np.empty([MAX_ARRAY_ROWS, 5], 'U50')
# expected structure: [Main, Type, Length, Time Happened, Quarter T+]
headingList = []  # storing info about game heading
homeList = []  # storing info about your team
visitorList = []  # storing info about the visitor team
homeScoreList = []
visitorScoreList = []
homeSaveList = []
visitorSaveList = []
homeGroundballList = []
visitorGroundballList = []
homeTurnoverList = []
visitorTurnoverList = []
homePenaltyList = []
visitorPenaltyList = []

with open('record.txt') as f:
    lines = [line.rstrip() for line in f]  # storing everything
f.close()

for home in lines:
    if home[0] != '#' and home[0] != '*':
        homeList.append(home)
    elif home[0] != '*':
        visitorList.append(home.replace('#', ''))


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


def get_home_score():
    linesLen = len(homeList)
    i = 0
    for x in range(linesLen):
        current = homeList[i]
        try:
            if current[0] == 'a':
                removed = homeList.pop(i)
                removed = removed[1:]
                homeScoreList.append(removed)
                i -= 1
        except IndexError:
            print("Current line is blank")
        i += 1
    # print(homeScoreList)
    # i, x = 0, 0  # reset var i, x

    for x in range(len(homeScoreList)):
        numbers = []
        split = homeScoreList[x].split(',')

        while (len(split[0]) <= 6):
            split[0] = str(split[0]) + "xx"

        for i in range(len(split[0])):
            numbers.append(split[0][i])

        homeScoreResult[x][0] = str(numbers[0]) + str(numbers[1])
        homeScoreResult[x][1] = str(numbers[2]) + str(numbers[3])
        homeScoreResult[x][2] = str(numbers[4]) + str(numbers[5])
        homeScoreResult[x][3] = split[1]
        homeScoreResult[x][4] = split[2]


def get_visitor_score():
    linesLen = len(visitorList)
    i = 0
    for x in range(linesLen):
        current = visitorList[i]
        try:
            if current[0] == 'a':
                removed = visitorList.pop(i)
                removed = removed[1:]
                visitorScoreList.append(removed)
                i -= 1
        except IndexError:
            print("Current line is blank")
        i += 1
    # print(visitorScoreList)
    # i, x = 0, 0  # reset var i, x

    for x in range(len(visitorScoreList)):
        numbers = []
        split = visitorScoreList[x].split(',')

        while len(split[0]) <= 6:
            split[0] = str(split[0]) + "xx"

        for i in range(len(split[0])):
            numbers.append(split[0][i])

        visitorScoreResult[x][0] = str(numbers[0]) + str(numbers[1])
        visitorScoreResult[x][1] = str(numbers[2]) + str(numbers[3])
        visitorScoreResult[x][2] = str(numbers[4]) + str(numbers[5])
        visitorScoreResult[x][3] = split[1]
        visitorScoreResult[x][4] = split[2]


def get_home_save():
    linesLen = len(homeList)
    i = 0
    for x in range(linesLen):
        current = homeList[i]
        try:
            if current[0] == 'g':
                removed = homeList.pop(i)
                removed = removed[1:]
                homeSaveList.append(removed)
                i -= 1
        except IndexError:
            print("Current line is blank")
        i += 1
    # print(homeScoreList)
    # i, x = 0, 0  # reset var i, x
    for x in range(len(homeSaveList)):
        split = homeSaveList[x].split(',')
        homeSaveResult[x][0] = split[0]
        homeSaveResult[x][1] = split[1]
        homeSaveResult[x][2] = split[2]


def get_visitor_save():
    linesLen = len(visitorList)
    i = 0
    for x in range(linesLen):
        current = visitorList[i]
        try:
            if current[0] == 'g':
                removed = visitorList.pop(i)
                removed = removed[1:]
                visitorSaveList.append(removed)
                i -= 1
        except IndexError:
            print("Current line is blank")
        i += 1
    # print(visitorScoreList)
    # i, x = 0, 0  # reset var i, x
    for x in range(len(visitorSaveList)):
        split = visitorSaveList[x].split(',')
        visitorSaveResult[x][0] = split[0]
        visitorSaveResult[x][1] = split[1]
        visitorSaveResult[x][2] = split[2]


def get_home_groundball():
    linesLen = len(homeList)
    i = 0
    for x in range(linesLen):
        current = homeList[i]
        try:
            if current[0] == 'b':
                removed = homeList.pop(i)
                removed = removed[1:]
                homeGroundballList.append(removed)
                i -= 1
        except IndexError:
            print("Current line is blank")
        i += 1
    # print(homeScoreList)
    # i, x = 0, 0  # reset var i, x
    for x in range(len(homeGroundballList)):
        split = homeGroundballList[x].split(',')
        if split[0] == '':
            split[0] = "xx"
        homeGroundballResult[x][0] = split[0]
        homeGroundballResult[x][1] = split[1]
        homeGroundballResult[x][2] = split[2]


def get_visitor_groundball():
    linesLen = len(visitorList)
    i = 0
    for x in range(linesLen):
        current = visitorList[i]
        try:
            if current[0] == 'b':
                removed = visitorList.pop(i)
                removed = removed[1:]
                visitorGroundballList.append(removed)
                i -= 1
        except IndexError:
            print("Current line is blank")
        i += 1
    # print(visitorScoreList)
    # i, x = 0, 0  # reset var i, x
    for x in range(len(visitorGroundballList)):
        split = visitorGroundballList[x].split(',')
        if split[0] == '':
            split[0] = "xx"
        visitorGroundballResult[x][0] = split[0]
        visitorGroundballResult[x][1] = split[1]
        visitorGroundballResult[x][2] = split[2]


def get_home_penalty():
    linesLen = len(homeList)
    i = 0
    for x in range(linesLen):
        current = homeList[i]
        try:
            if current[0] == 'p':
                removed = homeList.pop(i)
                removed = removed[1:]
                homePenaltyList.append(removed)
                i -= 1
        except IndexError:
            print("Current line is blank")
        i += 1
    # print(homeScoreList)
    # i, x = 0, 0  # reset var i, x
    # expected structure: [Main, Type, Length, Time Happened, Quarter T+]
    # input: p02t2
    for x in range(len(homePenaltyList)):
        split = homePenaltyList[x].split(',')
        homePenaltyResult[x][0] = split[0][0] + split[0][1]
        homePenaltyResult[x][1] = split[0][2]
        homePenaltyResult[x][2] = split[0][3]
        homePenaltyResult[x][3] = split[1]
        homePenaltyResult[x][4] = split[2]


def get_visitor_penalty():
    linesLen = len(visitorList)
    i = 0
    for x in range(linesLen):
        current = visitorList[i]
        try:
            if current[0] == 'p':
                removed = visitorList.pop(i)
                removed = removed[1:]
                visitorPenaltyList.append(removed)
                i -= 1
        except IndexError:
            print("Current line is blank")
        i += 1
    # print(visitorScoreList)
    # i, x = 0, 0  # reset var i, x
    # expected structure: [Main, Type, Length, Time Happened, Quarter T+]
    # input: p02t2
    for x in range(len(visitorPenaltyList)):
        split = visitorPenaltyList[x].split(',')
        visitorPenaltyResult[x][0] = split[0][0] + split[0][1]
        visitorPenaltyResult[x][1] = split[0][2]
        visitorPenaltyResult[x][2] = split[0][3]
        visitorPenaltyResult[x][3] = split[1]
        visitorPenaltyResult[x][4] = split[2]


def get_home_turnover():
    linesLen = len(homeList)
    i = 0
    for x in range(linesLen):
        current = homeList[i]
        try:
            if current[0] == 't':
                removed = homeList.pop(i)
                removed = removed[1:]
                homeTurnoverList.append(removed)
                i -= 1
        except IndexError:
            print("Current line is blank")
        i += 1
    # print(homeTurnoverList)
    # i, x = 0, 0  # reset var i, x

    for x in range(len(homeTurnoverList)):
        numbers = []
        split = homeTurnoverList[x].split(',')

        while (len(split[0]) <= 4):
            split[0] = str(split[0]) + "xx"

        for i in range(len(split[0])):
            numbers.append(split[0][i])
        # expected structure：[Who Caused, Who Dropped, Time Happened, Quarter T+]
        homeTurnoverResult[x][0] = str(numbers[0]) + str(numbers[1])
        homeTurnoverResult[x][1] = str(numbers[2]) + str(numbers[3])
        homeTurnoverResult[x][2] = split[1]
        homeTurnoverResult[x][3] = split[2]


def get_visitor_turnover():
    linesLen = len(visitorList)
    i = 0
    for x in range(linesLen):
        current = visitorList[i]
        try:
            if current[0] == 't':
                removed = visitorList.pop(i)
                removed = removed[1:]
                visitorTurnoverList.append(removed)
                i -= 1
        except IndexError:
            print("Current line is blank")
        i += 1
    # print(visitorTurnoverList)
    # i, x = 0, 0  # reset var i, x

    for x in range(len(visitorTurnoverList)):
        numbers = []
        split = visitorTurnoverList[x].split(',')

        while (len(split[0]) <= 4):
            split[0] = str(split[0]) + "xx"

        for i in range(len(split[0])):
            numbers.append(split[0][i])
        # expected structure：[Who Caused, Who Dropped, Time Happened, Quarter T+]
        visitorTurnoverResult[x][0] = str(numbers[0]) + str(numbers[1])
        visitorTurnoverResult[x][1] = str(numbers[2]) + str(numbers[3])
        visitorTurnoverResult[x][2] = split[1]
        visitorTurnoverResult[x][3] = split[2]


# Testing Area


get_heading()
print("HEADING")
print(headingResult)

get_home_score()
print("SELF SCORE")
print(homeScoreResult)

get_visitor_score()
print("OPPONENT SCORE")
print(visitorScoreResult)

get_home_save()
print("SELF SAVE")
print(homeSaveResult)

get_visitor_save()
print("OPPONENT SAVE")
print(visitorSaveResult)

get_home_groundball()
print("SELF GROUNDBALL")
print(homeGroundballResult)

get_visitor_groundball()
print("OPPONENT GROUNDBALL")
print(visitorGroundballResult)

get_home_penalty()
print("SELF PENALTY")
print(homePenaltyResult)

get_visitor_penalty()
print("OPPONENT PENALTY")
print(visitorPenaltyResult)

get_home_turnover()
print("SELF TURNOVER")
print(homeTurnoverResult)

get_visitor_turnover()
print("OPPONENT TURNOVER")
print(visitorTurnoverResult)

# Finished putting all the data in arrays
# Write in .xlsx

wb = Workbook()
filename = headingResult[0][0] + ' vs ' + headingResult[3][0] + '.xlsx'
ws1 = wb.active
ws1.title = "Scorebook"
heading = ['Home', 'Coach', 'Record', 'Visitor', 'Coach', 'Record']
ws1.merge_cells('A1:C1')
ws1['A1'] = "Team Information"
for x in range(6):
    ws1['A' + str(x + 2)] = heading[x]
    ws1.merge_cells('B' + str(x + 2) + ':' + 'C' + str(x + 2))
    ws1['B' + str(x + 2)] = headingResult[x][0]

wb.save(filename=filename)
