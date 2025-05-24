import tkinter as tk
from tkinter import filedialog
from des import decrypt, binary_to_string
from embed_in_image import extract_data_from_image

def decrypt_image():
    path = filedialog.askopenfilename()
    key = key_entry.get()
    binary = extract_data_from_image(path, 64)
    cipher = binary_to_string(binary)
    result = decrypt(cipher, key)
    output_label.config(text=f"המילה שהוסתרה: {result}")

# GUI
root = tk.Tk()
root.title("פענוח תמונה עם DES")

tk.Label(root, text="הזן מפתח:").pack()
key_entry = tk.Entry(root)
key_entry.pack()

tk.Button(root, text="בחר תמונה ופענח", command=decrypt_image).pack()

output_label = tk.Label(root, text="")
output_label.pack()

root.mainloop()
