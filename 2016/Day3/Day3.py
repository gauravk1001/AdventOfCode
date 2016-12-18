import re
import numpy as np

def read_file():
    with open("./input") as f:
        input = f.readlines()
    return input

def process_input(ip0, ip1, ip2):
    s0 = re.findall('[\d]+', ip0)
    s1 = re.findall('[\d]+', ip1)
    s2 = re.findall('[\d]+', ip2)
    pairs = np.array([s0, s1, s2])
    pairs = pairs.transpose()

    return pairs

def check_triangles(input):
    count = 0

    for i in xrange(0, len(input) - 2, 3):
        pairs = process_input(input[i], input[i + 1], input[i + 2])

        for combo in pairs:
            s0 = int(combo[0])
            s1 = int(combo[1])
            s2 = int(combo[2])

            if ((s0 + s1) > s2) and ((s1 + s2) > s0) and ((s2 + s0) > s1):
                count += 1

    return count

if __name__ == '__main__':
    print check_triangles(read_file())
