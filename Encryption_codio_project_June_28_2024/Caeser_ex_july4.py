

# Go through each letter in the message
# Create the result
result = ""
FIRST_CHAR = 65
LAST_CHAR_CODE = 90
CHAR_CHANGE = LAST_CHAR_CODE - FIRST_CHAR + 1

def caesar_shift(message, shift):
    global result  # Use the global result variable
    result = ""  # Reset the result for each message
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
    print(result)
usser_message = input("message to encrypte: ")
caesar_shift(usser_message, 2)


	

	

