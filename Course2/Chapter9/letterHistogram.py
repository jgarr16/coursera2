character = {'a': 0, 'b':0, 'c': 0, 'd':0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0, '1': 0, '2':0, '3': 0, '4':0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '0': 0}

string = raw_input('Input a string: ')
for spot in string:
	character[spot] = character[spot] + 1

for value in character:
	vals = character.values()
	if value > 0:
		print character[value],' - ',

