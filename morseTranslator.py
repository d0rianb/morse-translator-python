morseToAlphabet = {
    '-----': '0',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '.-': 'a',
    '-...': 'b',
    '-.-.': 'c',
    '-..': 'd',
    '.': 'e',
    '..-.': 'f',
    '--.': 'g',
    '....': 'h',
    '..': 'i',
    '.---': 'j',
    '-.-': 'k',
    '.-..': 'l',
    '--': 'm',
    '-.': 'n',
    '---': 'o',
    '.--.': 'p',
    '--.-': 'q',
    '.-.': 'r',
    '...': 's',
    '-': 't',
    '..-': 'u',
    '...-': 'v',
    '.--': 'w',
    '-..-': 'x',
    '-.--': 'y',
    '--..': 'z'
}

alphabetToMorse = { value: key for key, value in morseToAlphabet.items() }
acceptableLetters = [value for key, value in morseToAlphabet.items()]

class MorseTranslator:
    @staticmethod
    def sanitizeLetter(letter):
        if letter == ' ': return ''
        if not letter.lower() in acceptableLetters: return ''
        return alphabetToMorse[letter.lower()]

    @staticmethod
    def translate(text):
        sanitizeArray = list(map(MorseTranslator.sanitizeLetter, list(text)))
        return '/'.join(sanitizeArray)
