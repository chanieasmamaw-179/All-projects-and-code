import random
import string



chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)
def decrypt_char(cipher_text, chars, key):
	plain_text = ""
	for letter in cipher_text:
		if letter in key:
			index = key.index(letter)
			plain_text += chars[index]
		else:
			plain_text += letter  # If the character is not in `key`, keep it as is
	print(f"Decrypted message: {plain_text}")
	return plain_text
decrypt_char(chars, chars='a', key=3)