import base64


def bit64(PT):
    b = base64.b64encode(bytes(PT.encode('ascii')))
    base64_str = b.decode('utf-8')
    return b, base64_str


def initial_permutation(plaintext):
    initial_permutation_table = [
        58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7
    ]

    permuted_plaintext = ""
    for i in initial_permutation_table:
        permuted_plaintext += plaintext[i - 1]

    return permuted_plaintext


def initial_permutation_inv(block):
    ip_inv_table = [
        40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25
    ]
    plaintext = ""
    for i in range(len(ip_inv_table)):
        plaintext += block[ip_inv_table[i] - 1]
    return plaintext


print("ENTER PLAIN TEXT")
plain = input()
bas64, string64 = bit64(plain)
IP_input = "".join(["{:08b}".format(x) for x in bas64])
IP_input = IP_input[:64]
print(string64)
print(IP_input)
permuted_text = initial_permutation(IP_input)
print(permuted_text)
print(initial_permutation_inv(permuted_text))


def app():
    pass


if __name__ == '__main__':
    app()
