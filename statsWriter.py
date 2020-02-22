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
    quarterCount = 0
    quarterStart = 0
    while True:
        line = input("New Line: -, a000000, g00, b00, #\n")
        write_txt(line, quarterStart)
        line = list(line)
        side = 's'  # default self

        if line[0] == '#':  # opponent marking
            print("###OPPONENT Input###")
            line.pop(0)
            side = 'o'  # opponent
        else:
            print("---SELF Input---")

        if line[0] == 's':  # score
            print("SCORED")
        elif line[0] == 'a':
            print("ATTEMPTED SHOT")
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
        elif line[0] == 'c':
            print("GOALIE CLEAR FAILED")
            # clear success = Saved - Failed
        elif line[0] == '+':
            print("NEW QUARTER")
            quarterStart = time.strftime('%H%M%S', time.localtime(time.time()))
            quarterCount += 1
            print("QUARTER " + str(quarterCount))
        elif line[0] == '-':
            print("END QUARTER " + str(quarterCount))
        elif line[0] == '/':
            print("TIME OUT")
            # TODO Time Out Function
        elif line[0] == 'i':  # initializing
            write_txt("i NEW GAME HEADING i", quarterStart)
            home = input("Self Team?\n")
            write_txt(("i" + home), quarterStart)
            coach = input("Self Coach?\n")
            write_txt(("i" + coach), quarterStart)
            rec = input("Self Record? (Format:W-L-T)\n")
            write_txt(("i" + rec), quarterStart)
            visitor = input("Opponent Team?\n")
            write_txt(("i" + visitor), quarterStart)
            coach = input("Opponent Coach?\n")
            write_txt(("i" + coach), quarterStart)
            rec = input("Opponent Record? (Format:W-L-T)\n")
            write_txt(("i" + rec), quarterStart)
        elif line[0] == 'r':
            print("ROSTER")
        elif line[0] == 'q':
            sys.exit(0)


if __name__ == '__main__':
    main()
