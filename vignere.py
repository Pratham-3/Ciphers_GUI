def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return (key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    print(key)
    return "".join(key)


def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = ((ord(string[i])-97) +
             (ord(key[i])-97)) % 26
        x += 97
        cipher_text.append(chr(x))
    return "".join(cipher_text)


def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i])) % 26
        x += ord('A')

        orig_text.append(chr(x))
    return "".join(orig_text)


print("Enter the plain text")
string = input()
print("Enter key")
keyword = input()
key = generateKey(string, keyword)
cipher_text = cipherText(string, key)
print("Ciphertext :", cipher_text)
print("Original/Decrypted Text :", originalText(cipher_text, key))
