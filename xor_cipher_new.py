import itertools

def encode(plaintext,key):
	encoded_string_1 = "".join(chr(ord(plaintext_char) ^ ord(key_char)) for (plaintext_char,key_char) in itertools.izip(plaintext,itertools.cycle(key)))
