from sboxes import SBOXES


def string_to_binary(input_string):
    return ''.join([format(ord(char), '08b') for char in input_string])

def binary_to_string(binary_str):
    chars = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
    return ''.join([chr(int(char, 2)) for char in chars])

IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9,  1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

PC1 = [
    57, 49, 41, 33, 25, 17, 9,
    1,  58, 50, 42, 34, 26, 18,
    10, 2,  59, 51, 43, 35, 27,
    19, 11, 3,  60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7,  62, 54, 46, 38, 30, 22,
    14, 6,  61, 53, 45, 37, 29,
    21, 13, 5,  28, 20, 12, 4
]

PC2 = [
    14, 17, 11, 24, 1,  5,
    3,  28, 15, 6,  21, 10,
    23, 19, 12, 4,  26, 8,
    16, 7,  27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

SHIFTS = [
    1, 1, 2, 2, 2, 2, 2, 2,
    1, 2, 2, 2, 2, 2, 2, 1
]
E = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]
P = [
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25
]
FP = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9,  49, 17, 57, 25
]

def xor(a, b):
    return ''.join(['0' if bit_a == bit_b else '1' for bit_a, bit_b in zip(a, b)])
def sbox_substitution(xor_output):
    output = ''
    for i in range(8):
        block = xor_output[i*6:(i+1)*6]
        row = int(block[0] + block[5], 2)
        col = int(block[1:5], 2)
        val = SBOXES[i][row][col]
        output += format(val, '04b')
    return output
def f_function(R,K):
        expanded_R = permute(R, E)
        xor_result = xor(expanded_R, K)
        sbox_output = sbox_substitution(xor_result)
        return permute(sbox_output, P)



def permute(original, table):
    return ''.join([original[i - 1] for i in table])

def initial_permutation(binary_input):
    return ''.join([binary_input[i - 1] for i in IP])

def generate_keys(key_64bit):
    # PC-1: remove parity bits → 56 ביט
    key_56bit = permute(key_64bit, PC1)

    C = key_56bit[:28]
    D = key_56bit[28:]

    round_keys = []

    for shift in SHIFTS:
        # left circular shift
        C = C[shift:] + C[:shift]
        D = D[shift:] + D[:shift]

        combined = C + D
        round_key = permute(combined, PC2)
        round_keys.append(round_key)

    return round_keys


def encrypt(plaintext, key):
    binary_plaintext = string_to_binary(plaintext)
    binary_key = string_to_binary(key)

    permuted_plaintext = initial_permutation(binary_plaintext)
    L, R = permuted_plaintext[:32], permuted_plaintext[32:]

    round_keys = generate_keys(binary_key)

    for i in range(16):
        f_res = f_function(R, round_keys[i])
        L, R = R, xor(L, f_res)

    pre_output = R + L
    cipher_binary = permute(pre_output, FP)
    return binary_to_string(cipher_binary)

def decrypt(ciphertext, key):
    binary_cipher = string_to_binary(ciphertext)
    binary_key = string_to_binary(key)

    permuted_cipher = initial_permutation(binary_cipher)
    L, R = permuted_cipher[:32], permuted_cipher[32:]

    round_keys = generate_keys(binary_key)[::-1]  # reverse!

    for i in range(16):
        f_res = f_function(R, round_keys[i])
        L, R = R, xor(L, f_res)

    pre_output = R + L
    decrypted_binary = permute(pre_output, FP)
    return binary_to_string(decrypted_binary)



if __name__ == "__main__":
    plaintext = "thoughts"
    key = "nonsense"

    encrypted = encrypt(plaintext, key)
    print("Encrypted text:", encrypted)

    decrypted = decrypt(encrypted, key)
    print("Decrypted text:", decrypted)

    assert decrypted == plaintext, "Decryption failed!"





 


      


        