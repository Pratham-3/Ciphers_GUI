import random


# Function to generate a random key of specified length
def generate_key(length):
    key = ""
    for i in range(length):
        key += chr(random.randint(65, 90))
    return key


# Function to encrypt plaintext using Vernam Cipher
def vernam_cipher_encrypt(plain_text, key):
    cipher_text = ""
    for i in range(len(plain_text)):
        cipher_text += chr((ord(plain_text[i]) + ord(key[i])) % 26 + 65)
    return cipher_text


# Function to decrypt ciphertext using Vernam Cipher
def vernam_cipher_decrypt(cipher_text, key):
    plain_text = ""
    for i in range(len(cipher_text)):
        plain_text += chr((ord(cipher_text[i]) - ord(key[i])) % 26 + 65)
    return plain_text


# Example usage
print("Enter Plain Text: ")
plain_text = input()
key = generate_key(len(plain_text))
cipher_text = vernam_cipher_encrypt(plain_text, key)
decrypted_text = vernam_cipher_decrypt(cipher_text, key)

print("Plaintext:", plain_text)
print("Key:", key)
print("Ciphertext:", cipher_text)
print("Decrypted Text:", decrypted_text)


def app():
    pass


if __name__ == '__main__':
    app()
