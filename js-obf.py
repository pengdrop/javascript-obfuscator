'''
JS Obfuscator
Converts the JavaScript source code into obfuscated.
Developed by Safflower (https://github.com/Safflower/js-obfuscator)
using chars: !+/()[]{},
'''

import urllib.parse, urllib.request
import re


TABLE = dict()


def genStr(text):
	global TABLE
	if text in TABLE:
		return TABLE[text]
	else:
		res = []
		for val in text:
			res.append(TABLE.get(val, "'"+val+"'"))
		return "+".join(res)


def genAscArr(text):
	return [str(ord(i)) for i in text]


def genTable():
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
	TABLE['"'] = TABLE['']+'['+genStr('fontcolor')+']()['+TABLE['1']+'+('+TABLE[2]+')]'
	TABLE['<'] = TABLE['']+'['+genStr('sub')+']()['+TABLE[0]+']'
	TABLE['='] = TABLE['']+'['+genStr('fontcolor')+']()['+TABLE['1']+'+('+TABLE[1]+')]'
	TABLE['>'] = TABLE['']+'['+genStr('sub')+']()['+TABLE[4]+']'
	TABLE['/'] = TABLE['']+'['+genStr('sub')+']()['+TABLE[6]+']'
	TABLE['+'] = '(+('+TABLE[1]+'+'+TABLE['e']+'+['+TABLE[1]+']+('+TABLE[0]+')+('+TABLE[0]+'))+[])['+TABLE[2]+']'
	TABLE['.'] = '(+('+TABLE[1]+'+['+TABLE[1]+']+'+TABLE['e']+'+('+TABLE[2]+')+('+TABLE[0]+'))+[])['+TABLE[1]+']'
	TABLE[','] = '([]['+genStr('slice')+']['+genStr('call')+']'+TABLE['[object Object]']+'+[])['+TABLE[1]+']'

	TABLE['[object Window]'] = '([]['+genStr('filter')+']['+genStr('constructor')+']('+genStr('return self')+')()+[])'
	TABLE['W'] = TABLE['[object Window]']+'['+TABLE[8]+']'

	TABLE['h'] = '([]['+genStr('filter')+']['+genStr('constructor')+']('+genStr('return location')+')()+[])['+TABLE[0]+']'
	TABLE['p'] = '([]['+genStr('filter')+']['+genStr('constructor')+']('+genStr('return location')+')()+[])['+TABLE[3]+']'
	TABLE['m'] = '[]['+genStr('filter')+']['+genStr('constructor')+']('+genStr('return typeof 0')+')()['+TABLE[2]+']'

	TABLE['C'] = '[]['+genStr('filter')+']['+genStr('constructor')+']('+genStr('return escape')+')()('+TABLE['1']+'['+genStr("sub")+']())['+TABLE[2]+']'

	TABLE['('] = '([]['+genStr('filter')+']+[])['+genStr('trim')+']()['+TABLE['1']+'+('+TABLE[5]+')]'
	TABLE[')'] = '([]['+genStr('filter')+']+[])['+genStr('trim')+']()['+TABLE['1']+'+('+TABLE[6]+')]'
	TABLE['{'] = '([]['+genStr('filter')+']+[])['+genStr('trim')+']()['+TABLE['1']+'+('+TABLE[8]+')]'

	TABLE['g'] = '[]['+genStr('filter')+']['+genStr('constructor')+']('+genStr('return typeof""')+')()['+TABLE[5]+']'
	TABLE['%'] = '[]['+genStr('filter')+']['+genStr('constructor')+']('+genStr('return escape')+')()({})['+TABLE[0]+']'
	TABLE['B'] = '[]['+genStr('filter')+']['+genStr('constructor')+']('+genStr('return escape')+')()({})['+TABLE[2]+']'
	TABLE['S'] = '[]['+genStr('filter')+']['+genStr('constructor')+']('+genStr('return unescape')+')()('+TABLE['%']+'+'+TABLE['5']+'+('+TABLE[3]+'))'
	TABLE['x'] = '[]['+genStr('filter')+']['+genStr('constructor')+']('+genStr('return unescape')+')()('+TABLE['%']+'+'+TABLE['7']+'+('+TABLE[8]+'))'
	TABLE['v'] = '[]['+genStr('filter')+']['+genStr('constructor')+']('+genStr('return unescape')+')()('+TABLE['%']+'+'+TABLE['7']+'+('+TABLE[6]+'))'

	return


def obfuscate(code):
	global TABLE
	if len(TABLE) == 0: genTable()

	payload = ','.join(genStr(str(x)) for x in genAscArr(code))
	payload = '[]['+genStr('filter')+']['+genStr('constructor')+']('+genStr('return String')+')()['+genStr('fromCharCode')+']('+payload+')'
	payload = '[]['+genStr('filter')+']['+genStr('constructor')+']('+payload+')()'

	return payload


def main():
	code = 'alert("Hello, World!")'
	code = obfuscate(code)
	print(code)


if __name__ == '__main__':
	main()
