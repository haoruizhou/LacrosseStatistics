import numpy as np
import csv
import sys

names = np.array(
    [['00', 'Test 00'], ['02', 'Test 02'], ['03', 'Test 03'], ['04', 'Test 04'], ['09', 'Test 09'], ['18', 'Test 18']])


# player0 = main
# player1 = assist1
# player2 = assist2


def playerName(num):
    x = 0
    name = "ERROR"
    for x in range(len(names)):
        if num == names[x][0]:
            name = str(names[x][1])
            break
    return name


def writeCsv(content):
    with open("record.csv", "a") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(content)


def newQuarter():
    return


def score(main, a1, a2, side):
    # 加分到list，写进csv
    return 0


def main():
    while True:
        line = input("New Line: -, a000000, g00, b00, #\n")
        writeCsv(line)
        line = list(line)

        side = 's'  # default self

        if line[0] == '#':  # opponent marking
            print("###Opponent Input###")
            line.pop(0)
            side = 'o'  # opponent
        else:
            print("---Self Input---")

        if line[0] == 'a':  # score
            print("SCORED")
            line.pop(0)
            player0 = line[0] + line[1]
            player0name = playerName(player0)
            print(player0name + " scored.")
        elif line[0] == 'p':  # FO
            print("FACE-OFF WON")
            line.pop(0)
            player0 = line[0] + line[1]
            player0name = playerName(player0)
            print(player0name + " won face-off.")
        elif line[0] == 'b':  # ground ball
            print("GROUND BALL")
            line.pop(0)
            player0 = line[0] + line[1]
            player0name = playerName(player0)
            print(player0name + " picked up a ground ball.")
        elif line[0] == 'g':  # goalie save
            print("GOALIE SAVED")
            line.pop(0)
            player0 = line[0] + line[1]
            player0name = playerName(player0)
            print(player0name + " saved a ball.")
        elif line[0] == '-':
            print("NEW QUARTER")
            newQuarter()
            # if end quarter mark is needed?
        elif line[0] == 'q':
            sys.exit(0)


if __name__ == '__main__':
    main()
