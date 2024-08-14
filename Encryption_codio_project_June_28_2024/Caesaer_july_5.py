

# Encrypts a single character using a Caesar cipher with the given key.
def encrypt_char(char, key):
	if char.isalpha():
		start = ord('A') if char.isupper() else ord('a')
		new_char = chr(start + (ord(char) - start + key) % 26)
		return new_char
	else:
		return char
	
# Encrypts an entire text using a Caesar cipher with the given key.
def encrypt_text(text, key):
	encrypted_text = ''.join(encrypt_char(char, key) for char in text)
	return encrypted_text


# Decrypts a text encrypted with a Caesar cipher using the given key.
def decrypt_caesar(ciphertext, key):
	decrypted = ''.join(encrypt_char(char, -key) for char in ciphertext)
	return decrypted

# Main function calls and encrypted and decrypted messages are printed.
def main():
	user_text, key = ('LearniNg', 3)
	
	encrypted_text = encrypt_text(user_text, key)
	print(f"Encrypt_char({user_text}, {key})-->:", encrypted_text)
	
	decrypted_text = decrypt_caesar(encrypted_text, key)
	print(f"Dencrypt_char({encrypted_text}, {key})-->:", decrypted_text)


if __name__ == "__main__":
	main()
