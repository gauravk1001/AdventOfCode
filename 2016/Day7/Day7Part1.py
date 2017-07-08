import re
from collections import Counter
from pprint import pprint

def read_file():
	with open("./input.txt") as f:
		ip = f.readlines()
	return ip

def check_abba(ip, i, j):
#	print('checking for abba in ', ip[i:j])
	if j - i <= 3:
		return False
#	if '[' in ip[i:j] or ']' in ip[i:j]:
#		return False

	for k in range(0, j - i - 3, 1):
#		print ip[i + k], ip[i + k + 3], ip[i + k + 1], ip[i + k + 2]
		if (ip[i + k] == ip[i + k + 3]) and (ip[i + k + 1] == ip[i + k + 2]) and (ip[i + k] != ip[i + k + 1]):
#			print 'abba found'
			return True

	return False



def find_tls(full_input):
	tls_count = 0
	for ip in full_input:
		aib = False
		aob = False
#		print ip,
		obl = [pos for pos, char in enumerate(ip) if char == '[']
		cbl = [pos for pos, char in enumerate(ip) if char == ']']
		if not obl or not cbl:
			continue

#		print obl
#		print cbl
#		print obl[0], cbl[-1], len(ip)
		if (obl[0] == 0) or (cbl[-1] == (len(ip) - 2)):
			continue

		if len(obl) != len(cbl):
			print 'brackets dont match ... error'

		# check all strings within brackets
		for i in range(0, len(obl)):
			if check_abba(ip, obl[i] + 1, cbl[i]):
#				print 'abba not desirable, returning'
				aib = True
				break
		if aib:
			continue

		obl.insert(0, -1)
		obl.insert(len(obl), len(ip) - 1)
		cbl.insert(0, -1)
		cbl.insert(len(cbl), len(ip) - 1)
#		print obl
#		print cbl

		# check strings out of brackets
		for i in range(0, len(obl) - 1):

			lptr = cbl[i] + 1 #starting of string with ]
			rptr = obl[i + 1] #end of string with next [

			if check_abba(ip, lptr, rptr):
#				print 'abba found in seq'
				aob = True

			if aob:
				tls_count += 1
				break

#		print('tls_count:' + str(tls_count) + '\n')
	return tls_count


if __name__ == '__main__':
	print(find_tls(read_file()))
