import re
from collections import Counter

def read_file():
	with open("./input") as f:
		input = f.readlines()

	#print input
	return input

#def map_letters(sorted_letters):
#	for 

def find_sum_of_room_checksums(input):
	room_list = []
	bigsum = 0
	for line in input:
		split_string = re.findall(r'([a-z-]+)+(\d+)(\[[a-z]+\])\n', line)
		letters = ''.join(split_string[0][0].split('-'))
		numbers = split_string[0][1]
		checksum = split_string[0][2][1:-1]
		room_list.append([letters, numbers, checksum])

		#print ''.join(sorted(letters))
		sorted_letters = Counter(letters).items()
		sorted_letters.sort(key=lambda tup: tup[0])
		sorted_letters.sort(key=lambda tup: -tup[1])
		#print '\nletters, sorted-letters: ', letters, sorted_letters
		should_match_checksum = ''
		#for i in xrange(len(sorted_letters) - 1, len(sorted_letters) - 6, -1):
		for i in xrange(0, 5, 1):
			#print sorted_letters[i],
			should_match_checksum += sorted_letters[i][0]

		if should_match_checksum == checksum:
			bigsum += int(numbers)
			#print should_match_checksum, 'was valid', checksum, bigsum
		#else:
			#print should_match_checksum, 'was invalid', checksum, bigsum

	return bigsum

if __name__ == '__main__':
	print find_sum_of_room_checksums(read_file())
