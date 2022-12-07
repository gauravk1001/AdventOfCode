import heapq
import os

def find_most_calorie_elf(text):

    i = 0
    blob = ''
    
    current_elf_calories = 0
    max_elf_calories = 0
    list_cals = []

    while i < len(text):
        line = text[i]

        #print('curr line=' + line,)
        if line != '\n':
            i += 1
            
            current_elf_calories = add_calories_in_food(current_elf_calories, line)
            #print('total till now=' + str(current_elf_calories))

            # If we are not on the last line if the entire text, then continue
            if i <= len(text) - 1:
                continue

        list_cals.append(current_elf_calories)
            
        # Compare current count of cals to max cals found so far and update
        #print('total cals with this elf ' + str(current_elf_calories))
        #if current_elf_calories > max_elf_calories:
        #    max_elf_calories = current_elf_calories
        #    #print('max elf cals updated to ' + str(max_elf_calories))

        # reset blob to empty and increment to next line
        blob = ''
        i += 1
        current_elf_calories = 0

    heapq.heapify(list_cals)
    top_3_cals = heapq.nlargest(3, list_cals)

    #print('top 3 ' + str(top_3_cals))

    return sum(top_3_cals)
        
#def count_calories_with_elf(blob):

def add_calories_in_food(current_elf_calories, line):
    return current_elf_calories + int(line)


def get_input():
    print(os.getcwd())
    input_file = open(os.getcwd() + os.path.sep + "2022" + os.path.sep + "Day1" + os.path.sep + "input.txt", 'r')

    return input_file.readlines()

if __name__ == "__main__":
    print('total max cals =' + str(find_most_calorie_elf(get_input())))
