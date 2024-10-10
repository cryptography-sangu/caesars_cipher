
def caesar_cipher_encrypt(text,shift):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char)+shift - 65) % 26 +65)

        elif char.islower():
            result  += chr((ord(char)+shift - 97) % 26 +97)

        else:
            result += char

    return result

def caesar_cipher_decrypt(ciphertext,shift):
    return caesar_cipher_encrypt(ciphertext,-shift)




plaintext = "Hello World"
shift = 3
ciphertext = caesar_cipher_encrypt(plaintext,shift)
decrypted_text = caesar_cipher_decrypt(ciphertext,shift)
print("Plaintext:",plaintext)
print("Ciphertext:", ciphertext)
print("Decrypt:", decrypted_text)
