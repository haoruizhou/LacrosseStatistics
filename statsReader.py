import pandas as pd
import numpy as np
heading = np.array([[]])
headingList = []

with open('record.txt') as f:
    lines = [line.rstrip() for line in f]
    print(lines)
f.close()
print(len(lines))


for x in range(len(lines)):
    current = lines[x]
    try:
        if current[0] == 'i':
            headingList.append(lines.pop(x))
            x -= 1
    except IndexError:
        print("current line is blank")
    print(headingList)


print(headingList)
print(lines)


