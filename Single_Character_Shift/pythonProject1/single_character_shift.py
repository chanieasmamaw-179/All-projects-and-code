import random
import string


chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
print(chars)
key = chars.copy()
random.shuffle(key)
#print(f" chars : {chars}")
#print(f"key : {key}")
#Encription
plain_tex = input("Enter a message to encrypted")
cipher_text = " "

for letter in plain_tex:
	index = chars.index(letter)
	cipher_text += key[index]
print(f"orginal message: {plain_tex}")
print(f"encrypted message {cipher_text}")

#decryption
def decrypt_caesar(ciphertext, key)
plain_tex = input("Enter a message to encrypted")
plain_tex = " "

for letter in cipher_text:
	index = key.index(letter)
	plain_tex += chars[index]
print(f"encrypted message {cipher_text}")
print(f"orginal message: {plain_tex}")

