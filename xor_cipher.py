"""
simple example of an XOR cipher
http://www.wikipedia.org/xor_cipher
"""

message = ['t','e','s','t']
key = ['h','e','l','o']
encode = []
encoded_string = ""
plain_text = []
i = 0
for num in message:
	message[i] = ord(message[i])
	key[i] = ord(key[i])
	i+=1

i = 0
for index in message:
	encode.append(message[i] ^ key[i])
	i+=1

i = 0
for index in encode:
	encoded_string += chr(encode[i])
	plain_text.append(chr(encode[i] ^key[i]))
	i+=1
print encoded_string
print plain_text
