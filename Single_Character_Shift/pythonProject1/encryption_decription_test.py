import random
import string
def encrypt_char(chars, key):
	chars = " " + string.punctuation + string.digits + string.ascii_letters
	chars = list(chars)
	key = chars.copy()
	random.shuffle(key)
	
	plain_text = input("Enter a message to encrypt: ")
	cipher_text = ""
	
	for letter in plain_text:
		if letter in chars:
			index = chars.index(letter)
			cipher_text += key[index]
		else:
			cipher_text += letter  # If the character is not in `chars`, keep it as is
	
	print(f"Original message: {plain_text}")
	
	return cipher_text, chars, key

def decrypt_char(cipher_text, chars, key):
	plain_text = ""
	for letter in cipher_text:
		if letter in key:
			index = key.index(letter)
			plain_text += chars[index]
		else:
			plain_text += letter  # If the character is not in `key`, keep it as is
	
	print(f"Encrypted message: {cipher_text}")
	print(f"Decrypted message: {plain_text}")


def main():
	cipher_text, chars, key = encrypt_char('a', 3 == 'd')
	decrypt_char(cipher_text, chars, key)


if __name__ == "__main__":
	main()
