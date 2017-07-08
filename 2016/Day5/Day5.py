import sys, hashlib, time

def find_password(doorid):
	index = 0
	digits_done = 0
	password = ''
	password_dict = dict()
	while True:
		if digits_done == 8:
			print 'len of password was 8'
			break

		doorid_for_hash = doorid + str(index)
		makes_md5 = hashlib.md5()
		makes_md5.update(doorid_for_hash)
		hashed_doorid = makes_md5.hexdigest()

		if hashed_doorid.find('00000', 0 , 5) > -1:
			print 'full hash', hashed_doorid
			if str.isdigit(hashed_doorid[5]) and int(hashed_doorid[5]) >= 0 and int(hashed_doorid[5]) <= 8 and bool(password_dict.get(int(hashed_doorid[5]))) == False:
				password_dict[int(hashed_doorid[5])] = hashed_doorid[6]
				print 'current found letter in ', doorid_for_hash, 'is', hashed_doorid[5], 'and password is now', password_dict
				digits_done += 1

		index += 1

	for k, v in password_dict.iteritems():
		password = password + v
	return password

if __name__ == '__main__':
	start = time.time()
	print find_password(sys.argv[1])
	end = time.time()
	print 'time to run: ', ((end - start) / (1.0 * 60)), 'minutes'
