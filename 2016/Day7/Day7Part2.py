#!/usr/bin/python
# incorrect answers: 259, 287, 158
import re
from pprint import pprint

def read_file():
    with open("./input.txt") as f:
        ip = f.readlines()
        return ip

def count_tls(full_input):
    tls_count = 0
    for ip in full_input:
#        print ip,
        obl = [pos for pos, char in enumerate(ip) if char == '[']
        cbl = [pos for pos, char in enumerate(ip) if char == ']']

        # if no [ or ] found, reject it
        if not obl or not cbl:
            continue

        if len(obl) != len(cbl):
            print 'error: brackets dont match'

        # match any text inside brackets
        r1 = re.compile(r'\[([a-z]+)\]')
        inside = r1.findall(ip)
        # substitute anythign matched with ' '
        remaining = r1.sub(' ', ip)
#        print('inside brackets', inside, 'subbed', remaining)

        # split the string with text outside brackets and spaces on whitespace char
        r2 = re.compile(r'\s')
        outside = r2.split(remaining)
#        print('outside brackets', outside)

        # join 'inside text,outside text'
        inside = ''.join(inside)
        outside = ''.join(outside)
        one = outside + ',' + inside
#        print(one)

        # find ABA,BAB in the resultant single string
        r3 = re.compile(r'([a-z])((?!\1)[a-z])\1[a-z]*,[a-z]*\2\1\2')
        ssl = r3.findall(one)
#        print('support ssl', ssl)

        if ssl:
            tls_count += 1

#        print('tls_count:' + str(tls_count) + '\n')

    return tls_count

if __name__ == '__main__':
    print(count_tls(read_file()))
