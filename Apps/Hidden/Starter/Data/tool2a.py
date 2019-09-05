class encryptText:
    def __init__(self, text):
        self.text = text
    def encrypt(self):
        self.ciphertext = ""
        for letter in self.text:
            char = ord(letter)
            char = char + 2
            NewLetter = chr(char)
            self.ciphertext = self.ciphertext + NewLetter
    def decrypt(self):
        self.plaintext = ""
        for letter in self.text:
            char = ord(letter)
            char = char - 2
            NewLetter = chr(char)
            self.plaintext = self.plaintext + NewLetter