
def read_file():
    input_file = open("d:/GitHub/AdventOfCode/2020/Day1/input.txt", 'r')
    input = input_file.read()
    return input

def calc_total(input):

    nos = sorted([int(x) for x in input.split()])

    mul = 0
    print("nos", len(nos))

    for i in range(0, len(nos)):
        # print("\nnos[i]", nos[i])
        first = i + 1
        last = len(nos) - 1
        while last > i and first < len(nos):
            # print("nos[j]", nos[j], end=",")
            
            if (nos[i] + nos[first] + nos[last]) == 2020:
                mul = nos[i] * nos[first] * nos[last]
                print("3 nos ", nos[i], nos[first], nos[last])
                break

            if nos[i] + nos[first] + nos[last] < 2020:
                first += 1
                continue
            
            if nos[i] + nos[first] + nos[last] > 2020:
                last -= 1
                continue

    print("mul", mul)

if __name__ == "__main__":
    print("yoo")
    calc_total(read_file())
