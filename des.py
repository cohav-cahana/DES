def string_to_binary(input_string):
    return ''.join([format(ord(char), '08b') for char in input_string])

def binary_to_string(binary_str):
    chars = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
    return ''.join([chr(int(char, 2)) for char in chars])

if __name__ == "__main__":
    plaintext = "thoughts"
    key = "nonsense"

    binary_plaintext = string_to_binary(plaintext)
    binary_key = string_to_binary(key)

    print("Plaintext (binary):", binary_plaintext)
    print("Key (binary):", binary_key)

        