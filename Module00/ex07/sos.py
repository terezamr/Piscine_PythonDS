import sys

code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', 
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}

def morseCode(str):
    for char in str: #checks if every char exists in the dict
        if char.upper() not in code:
            raise AssertionError("character not found")
    for char in str:
        print(code[char.upper()], end = '')

def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError("Wrong number of arguments")

        # checks if the argument is a string
        try:
            arg = str(sys.argv[1])  # Convert to string
        except:
            raise AssertionError("Wrong type of arguments: expected a string")

        morseCode(arg)
    except AssertionError as e:
        print("AssertionError: ", str(e))

if __name__ == "__main__":
    main()