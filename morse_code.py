morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': '/',
    '!': '-.-.--', '"': '.-..-.', '&': '.-...', "'": '.----.', '(': '-.--.',
    ')': '-.--.-', '+': '.-.-.', ',': '--..--', '/': '-..-.', ':': '---...',
    '=': '-...-', '?': '..--..', '@': '.--.-.'
}


def plain_morse(plain: str) -> str:
    translated = ' '.join(morse_code_dict.get(char.upper()) for char in plain if char.upper() in morse_code_dict)
    return translated


def convert(morse_char: str) -> str:
    value_idx = list(morse_code_dict.values()).index(morse_char)
    return list(morse_code_dict.keys())[value_idx]


def morse_plain(morse: str) -> str:
    words = morse.split('/')
    translated_text = []

    for word in words:
        letters = word.split(' ')
        translated_word = ''.join(convert(letter) for letter in letters if letter)
        translated_text.append(translated_word)

    return ' '.join(translated_text)


def main() -> None:
    test = "hello world! It's me, Mario. #test"
    
    translated = plain_morse(test)
    print(f"Text to Morse: {translated}")

    re_translated = morse_plain(translated)
    print(f"Morse to Text: {re_translated}")


if __name__ == "__main__":
    main()