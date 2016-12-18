import re

log_x = []
log_y = []

keypad = [['0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '1', '0', '0', '0'],
            ['0', '0', '2', '3', '4', '0', '0'],
            ['0', '5', '6', '7', '8', '9', '0'],
            ['0', '0', 'A', 'B', 'C', '0', '0'],
            ['0', '0', '0', 'D', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0']]

def read_file():
    with open("input") as f:
        input = f.readlines()
    return input

def move(xstart, ystart, direction):

    if keypad[xstart][ystart] == '0':
        return (xstart, ystart)

    xnew = xstart
    ynew = ystart
    if direction == 'L':
        ynew = (ystart - 1) if keypad[xstart][ystart - 1] != '0' else ystart
        xnew = xstart
    elif direction == 'R':
        ynew = (ystart + 1) if keypad[xstart][ystart + 1] != '0' else ystart
        xnew = xstart
    elif direction == 'U':
        xnew = (xstart - 1) if keypad[xstart - 1][ystart] != '0' else xstart
        ynew = ystart
    elif direction == 'D':
        xnew = (xstart + 1) if keypad[xstart + 1][ystart] != '0' else xstart
        ynew = ystart

    # print 'moved'
    return (xnew, ynew)

def find_code(input):
    code = ''

    xstart = 3
    ystart = 1
    xnew = 3
    ynew = 1
    for line in input:
        print '\nstarted at ', xstart, ystart, ' and processing ', line
        # xnew = xstart
        # ynew = ystart
        for direction in line:
            xnew, ynew = move(xnew, ynew, direction)
            print xnew, ynew, '.',

        code = code + keypad[xnew][ynew]
        xstart = xnew
        ystart = ynew

    return code


if __name__ == '__main__':
    print find_code(read_file())
