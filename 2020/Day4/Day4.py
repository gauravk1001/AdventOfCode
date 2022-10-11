import re
import os

def check_valid_password(text):

    i = 0
    blob = ''
    required_fields = {
        'byr:': False,
        'iyr:': False,
        'eyr:': False,
        'hgt:': False,
        'hcl:': False,
        'ecl:': False,
        'pid:': False
        }
    count_passport = 0
    count_non_passport = 0

    while i < len(text):
        line = text[i]

        #print('curr line=' + line)
        if line != '\n':
            blob = blob + text[i]
            i += 1
            
            # If we are not on the last line if the entire text, then continue
            if i <= len(text) - 1:
                continue

        #print('line=' + blob)

        # Check if all the required_fields are in the current blob
        # Count the fields that are in the current blob too
        #field_count = 0
        for field in required_fields.keys():
            if field in blob:
                if not required_fields[field]:
                    required_fields[field] = True
                else:
                    #print('line contains many ' + field)
                    required_fields[field] = False
                    break
            else:
                #print('line does not contain' + field)
                #required_fields[field] = False
                break

        # current blob doesn't have all the required fields, then it is not a passport
        # even one single false in the dict, we dont have a passport
        if False in required_fields.values():
            count_non_passport += 1
            #print('line not pass' + str(count_non_passport))
        else: # it is a passport because all the required fields are in the blob
            count_passport += 1
            #print('line counted' + str(count_passport))

        # reset blob to empty and increment to next line
        blob = ''
        i += 1
        required_fields = required_fields.fromkeys(required_fields, False)
        #print('\n--')

    print('pass=' + str(count_passport))
    print('non pass=' + str(count_non_passport))


def get_input():
    print(os.getcwd())
    input_file = open(os.getcwd() + os.path.sep + "2020" + os.path.sep + "Day4" + os.path.sep + "input.txt", 'r')

    return input_file.readlines()


if __name__ == "__main__":
    check_valid_password(get_input())
