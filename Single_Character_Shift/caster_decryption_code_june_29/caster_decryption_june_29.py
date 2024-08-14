import random
import string


def encrypt_char(chars, key):
	chars = " " + string.punctuation + string.digits + string.ascii_letters
	chars = list(chars)
	key = chars.copy()
	random.shuffle(key)
	
	plain_text = "Jylbujm nby gimn zugiom nblyy qilxm onnylyx ch fcnylunoly, “Yn no, Vlony?” (Ypyh sio, Vlonom?) nbcm yrjlymmcih bum wigy xiqh ch bcmnils ni gyuh nby ofncguny vynlusuf vs ihy’m wfimymn zlcyhx. Nbcm mwyhy, ch qbcwb nby wihmjclunilm ch nby Myhuny ummummchuny Wuymul, cm ihy iz nby gimn xluguncw gigyhnm ih nby Mbueymjyulyuh mnuay. Nby uoxcyhwy bum domn qcnhymmyx nby ulliauhwy uhx bovlcm iz u lofyl qbi bum mioabn, qcnbch u lyjovfcw, ni vywigy u gihulwb, wigjulcha bcgmyfz ni nby aixm. Vlonom, u zlcyhx iz Wuymul uhx syn u guh qbi fipym Ligy (uhx zlyyxig) gily, bum dichyx nby wihmjclunilm ch nby ummummchuncih, u vynlusuf qbcwb cm wujnolyx vs nby nblyy qilxm uvipy ch nbcm zugiom Mbueymjyuly koiny."
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
	cipher_text, chars, key = encrypt_char('a', 3)
	decrypt_char(cipher_text, chars, key)


if __name__ == "__main__":
	main()
