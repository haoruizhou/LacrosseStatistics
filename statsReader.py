import pandas as pd
import numpy as np
heading = np.array([[]])
headingList = []

with open('record.txt') as f:
    lines = [line.rstrip() for line in f]
    print(lines)
f.close()

i = 0
linesLen = len(lines)
for x in range(linesLen):
    current = lines[i]
    try:
        if current[0] == 'i':
            headingList.append(lines.pop(i))
            i -= 1
    except IndexError:
        print("current line is blank")
    print(headingList)
    i += 1

print(headingList)
print(lines)


