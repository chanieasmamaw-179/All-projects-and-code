BOOK_FILE_NAME = "encrypted_book.txt"


# Function to read the book content from the file
def get_book_content(file_path):
	with open(file_path, "r") as handle:
		return handle.read()


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


# Main function to read the encrypted book, decrypt it, and print the result.
def main():
	# Read the encrypted book content
	encrypted_book = get_book_content(BOOK_FILE_NAME)
	
	# Decrypt the content using the provided key
	key = 3  # Assuming the key is 3, you can change it if needed
	decrypted_text = decrypt_caesar(encrypted_book, key)
	
	# Print the decrypted text
	print(decrypted_text[:500])


if __name__ == "__main__":
	main()
