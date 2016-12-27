import re
from collections import Counter

def read_file():
	with open("./input") as f:
		input = f.readlines()

	#print input
	return input

def find_sum_of_room_checksums(input):
	room_list = []
	bigsum = 0
	for line in input[:10]:
		# room = re.findall(r'^([a-z]+)-([a-z]+.{1})+(\d+)(\[[a-z]+\])\n$', line)
		split_string = re.findall(r'([a-z-]+)+(\d+)(\[[a-z]+\])\n', line)
		letters = ''.join(split_string[0][0].split('-'))
		numbers = split_string[0][1]
		checksum = split_string[0][2][1:-1]
		room_list.append([letters, numbers, checksum])

		sorted_letters = sorted(letters)
		#print '\nletters, sorted-letters: ', letters, sorted_letters,
		valid = True
		should_match_checksum = ''
		list_sorted_letters = sorted_letters.items()i
		ctr = 0
		print sorted_letters.iteritems()
		for k in sorted_letters:
			if ctr >= len(checksum):
				break

			print k, '; ',
			should_match_checksum += str(k)

			ctr += 1

		print should_match_checksum
		if should_match_checksum == checksum:
			bigsum += int(numbers)
			print split_string, 'was valid', checksum, valid, bigsum
		else:
			print split_string, 'was invalid', checksum, valid, bigsum

	#print room_list

	return len(room_list)

if __name__ == '__main__':
	print find_sum_of_room_checksums(read_file())
