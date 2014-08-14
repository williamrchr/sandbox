"""
simple one way hash
"""

string = str(raw_input("what do you want to hash?: "))

def hashme(string):
	while len(string) != 64:
		if len(string) < 64:
			#string += str(0)
			string +=chr(ord(string[len(string)-1])+1)
		elif len(string) > 64:
			new_string = string[0:64]
			string = new_string
	
	string_list = list(string)
	print string_list
	i=0
	for character in string_list:
		character = ord(character)
		string_list[i]= character
		i+=1
	print string_list
	
	A = string[0:4]
	B = string[4:8]
	C = string[8:12]
	D = string[12:16]
	E = string[16:20]
	F = string[20:24]
	G = string[24:28]
	H = string[28:32]
	I = string[32:36]
	J = string[36:40]
	K = string[40:44]
	L = string[44:48]
	M = string[48:52]
	N = string[52:56]
	O = string[56:60]
	P = string[60:64]
	
	
		
	
hashme(string)