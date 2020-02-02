import pandas as pd
import numpy as np

heading = np.empty([6, 3], 'U50')
# note: https://stackoverflow.com/questions/55377213/numpy-taking-only-first-character-of-string
# type str only takes the first character of string
# use U + length instead

headingList = []


with open('record.txt') as f:
    lines = [line.rstrip() for line in f]
    print(lines)
f.close()


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
    i = 0  # reset var i

    for x in range(len(headingList)):
        split = headingList[x].split(',')
        print(split)
        heading[x][0] = split[0]
        heading[x][1] = split[1]
        heading[x][2] = split[2]

    print(heading)


get_heading()