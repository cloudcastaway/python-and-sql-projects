class Convert():
    def __init__(self):
        # alpha-numeric symbols and some special chars - morse code chart
        self.chart = {"a": ".-", "b": "-...",
                "c": "-.-.", "d": "-..", "e": ".",
                "f": "..-.", "g": "--.", "h": "....",
                "i": "..", "j": ".---", "k": "-.-",
                "l": ".-..", "m": "--", "n": "-.",
                "o": "---", "p": ".--.", "q": "--.-",
                "r": ".-.", "s": "...", "t": "-",
                "u": "..-", "v": "...-", "w": ".--",
                "x": "-..-", "y": "-.--", "z": "--..",
                "1": ".----", "2": "..---", "3": "...--",
                "4": "....-", "5": ".....", "6": "-....",
                "7": "--...", "8": "---..", "9": "----.",
                "0": "-----", ", ": "--..--", ".": ".-.-.-",
                "?": "..--..", "/": "-..-.", "-": "-....-",
                "(": "-.--.", ")": "-.--.-", " ": "/"}
    
    # converts plain text into morse code
    def encrypt(self, input_text):
        morse_code = ""
        for char in input_text:
            morse_code += " "
            for key, value in self.chart.items():
                if char == key:
                    morse_code += value
                    break
        return morse_code
    
    def decrypt(self, input_morse_code):
        text = ""
        words_list = input_morse_code.split()
        for letter in words_list:
            for key, value in self.chart.items():
                if letter == value:
                    text += key
                    break
        return text
    
    def get_method(self, selected_method):
        if selected_method == "e":
            return "encrypt"
        else:
            return "decrypt"
    
    def get_chart(self):
        return self.chart