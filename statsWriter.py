import numpy as np
import time
import sys


names = np.array(
    [['00', 'Test 00'], ['02', 'Test 02'], ['03', 'Test 03'], ['04', 'Test 04'], ['09', 'Test 09'], ['18', 'Test 18']])
visitorPlayers = np.array([[]])
# TODO input visitor players list
# player0 = main
# player1 = assist1
# player2 = assist2


def write_txt(content, quarterStart):
    current = time.strftime('%H%M%S', time.localtime(time.time()))
    diff = int(current) - int(quarterStart)
    file = open("record.txt", "a")
    # input structure: what happened, current time, T+ quarter start
    # T+ need to convert seconds to min / hour (in statsReader.py)
    file.write(content + "," + str(current) + "," + str(diff) + "\n")
    file.close()


def main():
    quarterStart = 0
    while True:
        line = input("New Line: -, a000000, g00, b00, #\n")
        write_txt(line, quarterStart)
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
        elif line[0] == 'f':  # FO
            print("FACE-OFF WON")
        elif line[0] == 'b':  # ground ball
            print("GROUND BALL")
        elif line[0] == 't':
            print("TAKEOVER")
        elif line[0] == 'p':
            print("PENALTY")
        elif line[0] == 'g':  # goalie save
            print("GOALIE SAVED")
        elif line[0] == '+':
            print("NEW QUARTER")
            quarterStart = time.strftime('%H%M%S', time.localtime(time.time()))
        elif line[0] == '-':
            print("END QUARTER")
        elif line[0] == '/':
            print("TIME OUT")
            # TODO Time Out Function
        elif line[0] == 'i':  # initializing
            write_txt("i NEW GAME HEADING i", quarterStart)
            home = input("Home Team?\n")
            write_txt(("i" + home), quarterStart)
            coach = input("Home Coach?\n")
            write_txt(("i" + coach), quarterStart)
            rec = input("Home Record? (Format:W-L-T)\n")
            write_txt(("i" + rec), quarterStart)
            visitor = input("Visitor Team?\n")
            write_txt(("i" + visitor), quarterStart)
            coach = input("Visitor Coach?\n")
            write_txt(("i" + coach), quarterStart)
            rec = input("Visitor Record? (Format:W-L-T)\n")
            write_txt(("i" + rec), quarterStart)
        elif line[0] == 'r':
            print("ROSTER")
        elif line[0] == 'q':
            sys.exit(0)


if __name__ == '__main__':
    main()
