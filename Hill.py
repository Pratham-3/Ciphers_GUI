import numpy as np


def encrypt(plaintext, key):
    PT_matrix = [[(ord(ch) - 97) % 26] for ch in plaintext]
    print(PT_matrix)
    key_matrix = [[(ord(ch) - 97) % 26] for ch in key]
    print(key_matrix)

    CT_matrix = [[0 for i in range(len(PT_matrix[0]))] for j in range(len(key_matrix))]
    for i in range(len(key_matrix)):
        for j in range(len(PT_matrix[0])):
            for k in range(len(key_matrix[0])):
                CT_matrix[i][j] += key_matrix[i][k] * PT_matrix[k][j]

    ciphertext = ''.join(
        [chr((CT_matrix[i][j] % 26) + ord('A')) for i in range(len(CT_matrix)) for j in range(len(CT_matrix[0]))])
    return ciphertext, CT_matrix, key_matrix


def decrypt(ciphertext, key_matrix):
    inversekey = np.linalg.inv(key_matrix)
    PT_matrix = [[0 for i in range(len(ciphertext[0]))] for j in range(len(inversekey))]
    for i in range(len(inversekey)):
        for j in range(len(ciphertext[0])):
            for k in range(len(inversekey[0])):
                PT_matrix[i][j] += inversekey[i][k] * ciphertext[k][j]

    plaintext = ''.join(
        [chr((PT_matrix[i][j] % 26) + ord('A')) for i in range(len(PT_matrix)) for j in range(len(PT_matrix[0]))])
    return ciphertext


print("enter plain text")
PT = input()
print("enter key")
Key = input()
cipher, ciphertext, key_matrix = encrypt(PT, Key)
print("encrypted text:", cipher)


# print("Decrypted or original text:", decrypt(ciphertext, key_matrix))


def app():
    pass


if __name__ == '__main__':
    app()
