import re
import numpy as np

def read_file():
    with open("./input") as f:
        input = f.readlines()

    print input
    return input

def find_sum_of_room_checksums(input):

    room_list = []
    for line in input:
        # room = re.findall(r'^([a-z]+)-([a-z]+.{1})+(\d+)(\[[a-z]+\])\n$', line)
        room = re.findall(r'([a-z]+[-])+(\d+)(\[[a-z]+\])\n', line)
        room_list.append(room)

    print room_list

    return len(room_list)

if __name__ == '__main__':
    print find_sum_of_room_checksums(read_file())
