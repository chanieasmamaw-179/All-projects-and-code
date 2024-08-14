MESSAGE = """
Jylbujm nby gimn zugiom nblyy qilxm onnylyx ch fcnylunoly, "Yn no, Vlony?" (Ypyh sio, Vlonom?) nbcm yrjlymmcih bum wigy xiqh ch bcmnils ni gyuh nby ofncguny vynlusuf vs ihy'm wfimymn zlcyhx. Nbcm mwyhy, ch qbcwb nby wihmjclunilm ch nby Myhuny ummummchuny Wuymul, cm ihy iz nby gimn xluguncw gigyhnm ih nby Mbueymjyulyuh mnuay. Nby uoxcyhwy bum domn qcnhymmyx nby ulliauhwy uhx bovlcm iz u lofyl qbi bum mioabn, qcnbch u lyjovfcw, ni vywigy u gihulwb, wigjulcha bcgmyfz ni nby aixm. Vlonom, u zlcyhx iz Wuymul uhx syn u guh qbi fipym Ligy (uhx zlyyxig) gily, bum dichyx nby wihmjclunilm ch nby ummummchuncih, u vynlusuf qbcwb cm wujnolyx vs nby nblyy qilxm uvipy ch nbcm zugiom Mbueymjyuly koiny.
"""


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
def decrypt_text(ciphertext, key):
	decrypted_text = ''.join(encrypt_char(char, -key) for char in ciphertext)
	return decrypted_text


# Breaks the Caesar cipher by trying all possible shifts.
def break_caesar_cipher(ciphertext):
	for shift in range(26):
		decrypted_text = decrypt_text(ciphertext, shift)
		print(f"Shift {shift}: {decrypted_text}")


def main():
	key = 3
	
	# Encrypt the message
	encrypted_text = encrypt_text(MESSAGE, key)
	print(f"Encrypted: {encrypted_text}")
	
	# Decrypt the message
	decrypted_text = decrypt_text(encrypted_text, key)
	print(f"Decrypted: {decrypted_text}")
	
	# Attempt to break the cipher
	print("\nAttempting to break the cipher:")
	break_caesar_cipher(encrypted_text)


if __name__ == "__main__":
	main()
