#import urllib2

# def getPage():
#     url="http://adventofcode.com/2015/day/1/input"
#
#     req = urllib2.Request(url)
#     response = urllib2.urlopen(req)
#     return response.read()

def read_file():
    with open("input") as f:
        input = f.readlines()

    return input

def find_floor(input):
    floor = 0
    index = 0
    for letter in input[0]:
        index += 1

        if letter == '(':
            floor += 1
        elif letter == ')':
            floor -= 1

        if floor == -1:
            break

    return index

if __name__ == "__main__":
    print find_floor(read_file())
