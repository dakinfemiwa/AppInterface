import os,sys
import sqlite3



directory = os.getcwd()
os.chdir(directory + "\\Data")

link = "app3vyBPcNfb9yJY5"
link2 = "keyo7Gn0KX5IV0E8v"

print(os.getcwd())
sys.path.append(directory + "\\Data")

from tool2a import encryptText

Cipher = encryptText(link)
Cipher.encrypt()
print(Cipher.ciphertext)
text = Cipher.ciphertext
Cipher = encryptText(text)
Cipher.decrypt()
print(Cipher.plaintext)
text2 = Cipher.plaintext

Cipher = encryptText(link2)
Cipher.encrypt()
print(Cipher.ciphertext)
text3 = Cipher.ciphertext
Cipher = encryptText(text3)
Cipher.decrypt()
print(Cipher.plaintext)
text4 = Cipher.plaintext

