import re
from collections import Counter
from pprint import pprint

def read_file():
	with open("./input.txt") as f:
		ip = f.readlines()

	#print input
#	input = '''
#	bgpmxqws\n
#	mxvdaluh\n
#	wpgcrcix\n
#	djugxgak\n
#	'''
#	print ip
	return ip

def find_sum_of_room_checksums(ip):
	pos_list = [Counter() for i in xrange(len(ip[0]) - 1)]
#	for position in xrange(len(input[0])):
#		print position
#		pos_list = pos_list.append(Counter())
	print(pos_list)

	for line in ip:
		for i in xrange(len(line.strip())):
			pos_list[i] += Counter(line[i])

	message = ''

	for counter in pos_list:
		print counter
		message += counter.most_common()[-1][0]

	return message

if __name__ == '__main__':
	pprint(find_sum_of_room_checksums(read_file()), indent = 2)
