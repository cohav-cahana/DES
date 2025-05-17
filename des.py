

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

if __name__ == "__main__":
    plaintext = "thoughts"
    key = "nonsense"

    binary_plaintext = string_to_binary(plaintext)
    binary_key = string_to_binary(key)

    print("Plaintext:", binary_plaintext)
    print("Key:", binary_key)

 
    permuted_plaintext = initial_permutation(binary_plaintext)
    print("After Initial Permutation:", permuted_plaintext)
    L0 = permuted_plaintext[:32]
    R0 = permuted_plaintext[32:]
    print("L0:", L0)
    print("R0:", R0)

    round_keys = generate_keys(binary_key)
    print("Round keys:")
    for i, rk in enumerate(round_keys, 1):
        print(f"Round {i}: {rk}")




        