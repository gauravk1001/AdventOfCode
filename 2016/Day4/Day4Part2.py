import re

def read_file():
	with open("./input") as f:
		input = f.readlines()
	return input

def rotate(full_string, rotate_value):
	new_string = ''
	for  letter in full_string:
		if letter != '-':
			new_string += chr(((ord(letter) - 97 + rotate_value) % 26) + 97)
		else:
			new_string += chr(32)

	return new_string

def find_north_pole_objects(input):
	for line in input:
		split_string = re.findall(r'([a-z-]+)+(\d+)(\[[a-z]+\])\n', line)
		letters = split_string[0][0]
		numbers = split_string[0][1]
		print rotate(letters, int(numbers)), numbers
	return

if __name__ == '__main__':
	find_north_pole_objects(read_file())
