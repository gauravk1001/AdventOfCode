import re

log_x = []
log_y = []

def read_file():
    with open("input") as f:
        input = f.readlines()
    return input[0]

def get_heading(current, turn):
    if current == 'U':
        if turn == 'L':
            heading = 'L'
        else:
            heading = 'R'
    elif current == 'L':
        if turn == 'L':
            heading = 'D'
        else:
            heading = 'U'
    elif current == 'D':
        if turn == 'L':
            heading = 'R'
        else:
            heading = 'L'
    elif current == 'R':
        if turn == 'L':
            heading = 'U'
        else:
            heading = 'D'
    return heading

def check_log(x, y):
    # print 'logging', x, y
    ctr = -1
    for a,b in zip(log_x, log_y):
        ctr += 1
        if x == a and y == b:
            # print 'match at index', ctr + 1
            return True

    log_x.append(x)
    log_y.append(y)

    # print log_x, '\n', log_y

    return False

def find_distance(input):
    # input = 'R4, L19, R3, L5, R10, L1, R4, R9'
    # input = 'L2, L3, R8, R4, R4, R8'
    directions = re.findall('[L|R][\d]+', input)

    current = 'U'
    x = 0
    y = 0

    # loop to run for each direction
    for direction in directions:
        # print '\nprocessing ', direction

        # get the direction for the head
        heading = get_heading(current, direction[0])

        # save the initial state for traversal
        xprev = x
        yprev = y

        # + or - steps and the number of steps initially
        pn = 0
        xsteps = 0
        ysteps = 0
        stop = False

        # determine the resultant direction and steps in that direction
        if heading == 'U':
            ysteps = int(direction[1:])
            pn = 1
            y += ysteps
        elif heading == 'L':
            xsteps = int(direction[1:])
            pn = -1
            x -= xsteps
        elif heading == 'D':
            ysteps = int(direction[1:])
            pn = -1
            y -= ysteps
        elif heading == 'R':
            xsteps = int(direction[1:])
            pn = 1
            x += xsteps

        # check the direction that the movement was in
        if xsteps == 0:
            steps = ysteps
        else:
            steps = xsteps

        # log the steps in (x, y) as visited
        for i in xrange(1, steps + 1):
            if xsteps == 0:
                if check_log(xprev, yprev + pn * i):
                    # print 'already visited ', xprev, yprev + pn * i
                    xstop = xprev
                    ystop = yprev + pn * i
                    stop = True
                    break
            elif ysteps == 0:
                if check_log(xprev + pn * i, yprev):
                    # print 'already visited ', xprev + pn * i, yprev
                    xstop = xprev + pn * i
                    ystop = yprev
                    stop = True
                    break

        if stop:
            break

        current = heading

    dist = 0
    if xstop !=0 or ystop != 0:
        dist = abs(xstop) + abs(ystop)
    else:
        dist = 'did not intersect before final destination'

    return dist

if __name__ == "__main__":
    print find_distance(read_file())
