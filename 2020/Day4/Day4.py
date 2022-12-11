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
    required_fields_count = required_fields.fromkeys(required_fields, 0)

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

        print('line=' + blob)

        # Check if all the required_fields are in the current blob
        # Count the fields that are in the current blob too
        #field_count = 0
        for field in required_fields.keys():
            if field in blob:
                if required_fields_count[field] == 0 and not required_fields[field]:
                    reg = field + '([a-z0-9#]+)'
                    values = re.search(reg, blob)
                    print('val found for ' + field + ' = ' + str(values))

                    # Validating the field contains value as per the rules
                    # If valid, returns true, else false
                    bool = validateFields(field[0:-1], values.group(1))
                    #print('val fields returns=' + str(bool))
                    # Mark the field as true or false from validation
                    required_fields[field] = bool
                    required_fields_count[field] += 1

                elif required_fields_count[field] > 0:

                    print('current field ' +  field + 'while line already has it')
                    break
            else:
                print('line does not contain' + field)
                required_fields[field] = False
                break

        #print('req fields=')
        #print(required_fields)
        # current blob doesn't have all the required fields, then it is not a passport
        # even one single false in the dict, we dont have a passport
        if False in required_fields.values():
            count_non_passport += 1
            print('line not pass' + str(count_non_passport))
        else: # it is a passport because all the required fields are in the blob
            count_passport += 1
            print('line counted' + str(count_passport))

        # reset blob to empty and increment to next line
        blob = ''
        i += 1
        required_fields = required_fields.fromkeys(required_fields, False)
        required_fields_count = required_fields.fromkeys(required_fields, 0)
        print('count of pass=' + str(count_passport))
        print('count of non pass=' + str(count_non_passport))
        print('\n--')

    print('pass=' + str(count_passport))
    print('non pass=' + str(count_non_passport))

def validateFields(field, value):
    ecls = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    #print('field in validateFields' + field + ' ' + value)
    if field == 'byr':
        if len(value) <= 4 and int(value) >= 1920 and int (value) <= 2002:
            #print('valid byr' + value)
            return True
    elif field == 'iyr':
        if len(value) <= 4 and int(value) >= 2010 and int (value) <= 2020:
            #print('valid iyr' + value)
            return True
    elif field == 'eyr':
        if len(value) <= 4 and int(value) >= 2020 and int (value) <= 2030:
            #print('valid eyr' + value)
            return True
    elif field == 'hgt':
        #print('hgt num=' + str(value[0:-2]) + ' ' + value[-2:] + 'haha')
        if value[-2:] == 'cm':
            if int(value[0:-2]) >= 150 and int(value[0:-2]) <= 193:
                #print('valid hgt' + value)
                return True
        elif value[-2:] == 'in':
            if int(value[0:-2]) >= 59 and int(value[0:-2]) <= 76:
                #print('valid hgt' + value)
                return True
    elif field == 'hcl':
        matches = re.search('(#[0-9a-f]{6})', value)
        if matches is not None:
            #print('matched=' + matches.group(0))
            return True
    elif field == 'ecl':
        if value in ecls:
            #print('ecl=' + value)
            return True
    elif field == 'pid':
        matches = re.search('([0-9]{9})', value)
        if matches is not None:
            #print('matched=' + matches.group(0))
            return True
    
    return False

def get_input():
    print(os.getcwd())
    input_file = open(os.getcwd() + os.path.sep + "2020" + os.path.sep + "Day4" + os.path.sep + "input copy.txt", 'r')

    return input_file.readlines()


if __name__ == "__main__":
    check_valid_password(get_input())
    # #required_fields = {
    #     'byr:': False,
    #     'iyr:': False,
    #     'eyr:': False,
    #     'hgt:': False,
    #     'hcl:': False,
    #     'ecl:': False,
    #     'pid:': False
    #     }
    #required_fields_count = required_fields.fromkeys(required_fields, 0)
    #print(required_fields_count)
