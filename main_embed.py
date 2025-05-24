from des import encrypt, decrypt, string_to_binary, binary_to_string
from embed_in_image import embed_data_in_image, extract_data_from_image

plaintext = "thoughts"
key = "nonsense"

cipher = encrypt(plaintext, key)
print("Encrypted text:", cipher)

binary_cipher = string_to_binary(cipher)
embed_data_in_image("secret_image.png", binary_cipher, "encoded_image.png")
print("✔️ Cipher embedded into encoded_image.png")

extracted_binary = extract_data_from_image("encoded_image.png", len(binary_cipher))
recovered_cipher = binary_to_string(extracted_binary)
decrypted = decrypt(recovered_cipher, key)

print("Recovered Cipher:", recovered_cipher)
print("Decrypted text:", decrypted)
