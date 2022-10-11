import re;

def check_valid_password():
    input_file = open("d:/GitHub/AdventOfCode/2020/Day2/input.txt", 'r')

    while True:
        line = input_file.readline()
        if not line:
            break

        print('line' + line)
        c = re.compile(r'(\d)-(\d)\s([a-z]):\s([a-z]+)')

        valid_count = 0

        matched = c.match(line)
        print(matched)
        mini =  matched.group(1)
        maxi = matched.group(2)
        char = matched.group(3)
        password = matched.group(4)
        print('grp:' + matched.group(), 'parts:', mini, maxi, char, password)

        mini = int(mini)
        maxi = int(maxi)
        count = password.count('char')
        if mini < count and count < maxi:
            valid_count += 1

        print("valid:", valid_count)

    

if __name__ == "__main__":
    check_valid_password()
