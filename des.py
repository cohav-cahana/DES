

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


def initial_permutation(binary_input):
    return ''.join([binary_input[i - 1] for i in IP])


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




        