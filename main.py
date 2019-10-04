#!/usr/bin/env python3

import sys

TABLE = dict()

def generate_string(text):
	global TABLE

	if text in TABLE:
		return TABLE[text]
	else:
		res = []
		for val in text:
			res.append(TABLE.get(val, "'"+val+"'"))
		return "+".join(res)


def generate_ascii_array(text):
	return [str(ord(i)) for i in text]


def generate_table():
	global TABLE

	TABLE[0] = '+[]'
	TABLE[1] = '+!![]'
	TABLE[2] = '!![]+!![]'
	TABLE[3] = '!![]+!![]+!![]'
	TABLE[4] = '!![]+!![]+!![]+!![]'
	TABLE[5] = '!![]+!![]+!![]+!![]+!![]'
	TABLE[6] = '!![]+!![]+!![]+!![]+!![]+!![]'
	TABLE[7] = '!![]+!![]+!![]+!![]+!![]+!![]+!![]'
	TABLE[8] = '!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]'
	TABLE[9] = '!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]'

	TABLE['0'] = '('+TABLE[0]+'+[])'
	TABLE['1'] = '('+TABLE[1]+'+[])'
	TABLE['2'] = '('+TABLE[2]+'+[])'
	TABLE['3'] = '('+TABLE[3]+'+[])'
	TABLE['4'] = '('+TABLE[4]+'+[])'
	TABLE['5'] = '('+TABLE[5]+'+[])'
	TABLE['6'] = '('+TABLE[6]+'+[])'
	TABLE['7'] = '('+TABLE[7]+'+[])'
	TABLE['8'] = '('+TABLE[8]+'+[])'
	TABLE['9'] = '('+TABLE[9]+'+[])'

	TABLE[''] = '([]+[])'
	TABLE['true'] = '(!![]+[])'
	TABLE['false'] = '(![]+[])'
	TABLE['NaN'] = '(+[![]]+[])'
	TABLE['NaN'] = '(+{}+[])'
	TABLE['undefined'] = '([][[]]+[])'
	TABLE['[object Object]'] = '({}+[])'

	TABLE['a'] = TABLE['false']+'['+TABLE[1]+']'
	TABLE['b'] = TABLE['[object Object]']+'['+TABLE[2]+']'
	TABLE['c'] = TABLE['[object Object]']+'['+TABLE[5]+']'
	TABLE['d'] = TABLE['undefined']+'['+TABLE[2]+']'
	TABLE['e'] = TABLE['true']+'['+TABLE[3]+']'
	TABLE['Infinity'] = '(+('+TABLE[1]+'+'+TABLE['e']+'+('+TABLE[1]+')+('+TABLE[0]+')+('+TABLE[0]+')+('+TABLE[0]+'))+[])'
	TABLE['f'] = TABLE['false']+'['+TABLE[0]+']'
	TABLE['i'] = TABLE['undefined']+'['+TABLE[5]+']'
	TABLE['j'] = TABLE['[object Object]']+'['+TABLE[3]+']'
	TABLE['l'] = TABLE['false']+'['+TABLE[2]+']'
	TABLE['n'] = TABLE['undefined']+'['+TABLE[1]+']'
	TABLE['o'] = TABLE['[object Object]']+'['+TABLE[1]+']'
	TABLE['r'] = TABLE['true']+'['+TABLE[1]+']'
	TABLE['s'] = TABLE['false']+'['+TABLE[3]+']'
	TABLE['t'] = TABLE['true']+'['+TABLE[0]+']'
	TABLE['u'] = TABLE['true']+'['+TABLE[2]+']'
	TABLE['y'] = TABLE['Infinity']+'['+TABLE[7]+']'

	TABLE['I'] = TABLE['Infinity']+'['+TABLE[0]+']'
	TABLE['N'] = TABLE['NaN']+'['+TABLE[0]+']'
	TABLE['O'] = TABLE['[object Object]']+'['+TABLE[8]+']'

	TABLE[','] = '[[],[]]+[]'
	TABLE['['] = TABLE['[object Object]']+'['+TABLE[0]+']'
	TABLE[']'] = TABLE['[object Object]']+'['+TABLE['1']+'+('+TABLE[4]+')]'
	TABLE[' '] = TABLE['[object Object]']+'['+TABLE[7]+']'
	TABLE['"'] = TABLE['']+'['+generate_string('fontcolor')+']()['+TABLE['1']+'+('+TABLE[2]+')]'
	TABLE['<'] = TABLE['']+'['+generate_string('sub')+']()['+TABLE[0]+']'
	TABLE['='] = TABLE['']+'['+generate_string('fontcolor')+']()['+TABLE['1']+'+('+TABLE[1]+')]'
	TABLE['>'] = TABLE['']+'['+generate_string('sub')+']()['+TABLE[4]+']'
	TABLE['/'] = TABLE['']+'['+generate_string('sub')+']()['+TABLE[6]+']'
	TABLE['+'] = '(+('+TABLE[1]+'+'+TABLE['e']+'+['+TABLE[1]+']+('+TABLE[0]+')+('+TABLE[0]+'))+[])['+TABLE[2]+']'
	TABLE['.'] = '(+('+TABLE[1]+'+['+TABLE[1]+']+'+TABLE['e']+'+('+TABLE[2]+')+('+TABLE[0]+'))+[])['+TABLE[1]+']'
	TABLE[','] = '([]['+generate_string('slice')+']['+generate_string('call')+']'+TABLE['[object Object]']+'+[])['+TABLE[1]+']'

	TABLE['[object Window]'] = '([]['+generate_string('filter')+']['+generate_string('constructor')+']('+generate_string('return self')+')()+[])'
	TABLE['W'] = TABLE['[object Window]']+'['+TABLE[8]+']'

	TABLE['h'] = '([]['+generate_string('filter')+']['+generate_string('constructor')+']('+generate_string('return location')+')()+[])['+TABLE[0]+']'
	TABLE['p'] = '([]['+generate_string('filter')+']['+generate_string('constructor')+']('+generate_string('return location')+')()+[])['+TABLE[3]+']'
	TABLE['m'] = '[]['+generate_string('filter')+']['+generate_string('constructor')+']('+generate_string('return typeof 0')+')()['+TABLE[2]+']'

	TABLE['C'] = '[]['+generate_string('filter')+']['+generate_string('constructor')+']('+generate_string('return escape')+')()('+TABLE['1']+'['+generate_string("sub")+']())['+TABLE[2]+']'

	TABLE['('] = '([]['+generate_string('filter')+']+[])['+generate_string('trim')+']()['+TABLE['1']+'+('+TABLE[5]+')]'
	TABLE[')'] = '([]['+generate_string('filter')+']+[])['+generate_string('trim')+']()['+TABLE['1']+'+('+TABLE[6]+')]'
	TABLE['{'] = '([]['+generate_string('filter')+']+[])['+generate_string('trim')+']()['+TABLE['1']+'+('+TABLE[8]+')]'

	TABLE['g'] = '[]['+generate_string('filter')+']['+generate_string('constructor')+']('+generate_string('return typeof""')+')()['+TABLE[5]+']'
	TABLE['%'] = '[]['+generate_string('filter')+']['+generate_string('constructor')+']('+generate_string('return escape')+')()({})['+TABLE[0]+']'
	TABLE['B'] = '[]['+generate_string('filter')+']['+generate_string('constructor')+']('+generate_string('return escape')+')()({})['+TABLE[2]+']'
	TABLE['S'] = '[]['+generate_string('filter')+']['+generate_string('constructor')+']('+generate_string('return unescape')+')()('+TABLE['%']+'+'+TABLE['5']+'+('+TABLE[3]+'))'
	TABLE['x'] = '[]['+generate_string('filter')+']['+generate_string('constructor')+']('+generate_string('return unescape')+')()('+TABLE['%']+'+'+TABLE['7']+'+('+TABLE[8]+'))'
	TABLE['v'] = '[]['+generate_string('filter')+']['+generate_string('constructor')+']('+generate_string('return unescape')+')()('+TABLE['%']+'+'+TABLE['7']+'+('+TABLE[6]+'))'

	return


def obfuscate(code):
	global TABLE
	if len(TABLE) == 0:
		generate_table()

	payload = ','.join(generate_string(str(x)) for x in generate_ascii_array(code))
	payload = '[]['+generate_string('filter')+']['+generate_string('constructor')+']('+generate_string('return String')+')()['+generate_string('fromCharCode')+']('+payload+')'
	payload = '[]['+generate_string('filter')+']['+generate_string('constructor')+']('+payload+')()'

	return payload


def main():
	if len(sys.argv) != 2:
		print('Usage: python main.py <filepath>')
		return

	with open(sys.argv[1], 'r') as f:
		before = f.read()

	after = obfuscate(before)
	print(after)


if __name__ == '__main__':
	main()
