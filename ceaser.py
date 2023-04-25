print("enter plain text: ")
plain_t = input()
print("enter key: ")
key = int(input())
cipher_t = ""

for i in range(len(plain_t)):
    index = plain_t[i]

    if index.isupper():
        cipher_t += chr((ord(index) + key - 65) % 26 + 65)

    else:
        cipher_t += chr((ord(index) + key - 97) % 26 + 97)


print("Encrypted text: ", cipher_t)
decrypted = ""
for i in range(len(cipher_t)):
    index = cipher_t[i]

    if index.isupper():
        decrypted += chr((ord(index) - key - 65) % 26 + 65)
    else:
        decrypted += chr((ord(index) - key - 97) % 26 + 97)



print("Decrypted text: ", decrypted)
