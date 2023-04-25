def railfence(PT):
    rail = [['\n' for i in range(len(PT))]
            for j in range(2)]

    dir_down = False
    row, col = 0, 0

    for i in range(len(PT)):
        if (row == 0) or (row == 1):
            dir_down = not dir_down
        rail[row][col] = PT[i]
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    print(rail)
    result = []
    for i in range(2):
        for j in range(len(PT)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    print(result)
    return "".join(result)


def derailfence(CT):
    rail = [['\n' for i in range(len(CT))]
            for j in range(2)]

    dir_down = None
    row, col = 0, 0

    for i in range(len(CT)):
        if row == 0:
            dir_down = True
        if row == 1:
            dir_down = False

        rail[row][col] = '*'
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(2):
        for j in range(len(CT)):
            if ((rail[i][j] == '*') and
                    (index < len(CT))):
                rail[i][j] = CT[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(CT)):

        if row == 0:
            dir_down = True
        if row == 1:
            dir_down = False
        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    return "".join(result)


if __name__ == "__main__":
    print("enter the plain text:")
    plaintext = input()
    ciphertext = railfence(plaintext)
    print("cipher text:", ciphertext)
    print("decrypted text:", derailfence(ciphertext))
