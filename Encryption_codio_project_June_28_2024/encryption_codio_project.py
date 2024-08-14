import random
import string

result = ""
FIRST_CHAR = 65
LAST_CHAR_CODE = 90
CHAR_CHANGE = LAST_CHAR_CODE - FIRST_CHAR + 1
char = " " + string.punctuation + string.digits + string.ascii_letters
char = list(char)
key = char.copy()
random.shuffle(key)

def caesar_shift(message, shift):
    global result  # Use the global result variable
    result = ""  # Reset the result for each message
    FIRST_CHAR = ord('A')
    LAST_CHAR_CODE = ord('Z')
    CHAR_CHANGE = 26
    
    
    for char in message.upper():
        if char.isalpha():
            char_code = ord(char)
            new_char_code = char_code + shift
            if new_char_code > LAST_CHAR_CODE:
                new_char_code -= CHAR_CHANGE
            if new_char_code < FIRST_CHAR:
                new_char_code += CHAR_CHANGE
            new_char = chr(new_char_code)
            result += new_char
        else:
            result += char
    print(f" encrypt_caesar ('A', 3 ) --> {result.lower()}")


user_message = 'A'
caesar_shift(user_message, 3)





"""

# Define character set including space, punctuation, digits, and letters
char = " " + string.punctuation + string.digits + string.ascii_letters
char = list(char)
key = char.copy()
random.shuffle(key)


def encrypt_message(char, key):
	plain_text = input("Enter a message to encrypt: ")
	cipher_text = ""
	
	for letter in char:
		if letter in char:
			index = char.index(letter)
			cipher_text += key[index]
		else:
			cipher_text += letter  # If the character is not in `chars`, keep it as is
	
	return cipher_text, char, key


def decrypt_message(cipher_text, char, key):
	plain_text = ""
	for letter in cipher_text:
		if letter in key:
			index = key.index(letter)
			plain_text += char[index]
		else:
			plain_text += letter  # If the character is not in `key`, keep it as is
	
	return plain_text


def main():
	cipher_text, char, key = encrypt_message('a', 3)
	print(f"Encrypted message: {cipher_text}")
	decrypted_message = decrypt_message(cipher_text, char, key)
	print(f"Decrypted message: {decrypted_message}")


if __name__ == "__main__":
	main()
"""