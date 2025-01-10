from art import caeser_cipher_art as art
alphabets = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "0", 
    "1", 
    "2", 
    "3", 
    "4", 
    "5", 
    "6", 
    "7", 
    "8", 
    "9"
]

def caesar_cipher(original: str, shift: int, operation: str):
    cipher_message = ""
    alphabets_length = len(alphabets) - 1
    for letter in original:
        if letter in alphabets:
            
            current_letter_index = alphabets.index(letter)
            shift_index = 0
            
            if operation == "encode":
                shift_index = current_letter_index + shift
            else:
                shift_index = current_letter_index - shift
                
            while shift_index > alphabets_length:
                shift_index = shift_index - alphabets_length
            cipher_message += alphabets[shift_index]
        else:
            cipher_message += letter
    print(f"Here is the {operation}d result: {cipher_message}")

restart = False
print(art)
while not restart:
    direction = input("Type 'encode' to encode or 'decode' to decode the message.\n").lower()
    if direction == "encode" or direction == "decode":
        text = input(f"Type your message to {direction}:\n")
        shift = int(input("Type the shift number.\n"))
        caesar_cipher(original= text, shift= shift, operation= direction)
    else:
        print("Please type the correct keyword!")
    
    continue_cipher = input("Want to cipher another message? Type 'yes' for yes, 'no' for no.\n").lower()
    restart = continue_cipher != "yes"
        