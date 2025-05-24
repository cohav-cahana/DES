from PIL import Image

def embed_data_in_image(image_path, binary_data, output_path):
    img = Image.open(image_path)
    pixels = img.load()
    
    width, height = img.size
    max_bits = width * height * 3
    if len(binary_data) > max_bits:
        raise ValueError("Message too long for the image.")

    data_index = 0
    for y in range(height):
        for x in range(width):
            if data_index >= len(binary_data):
                break
            r, g, b = pixels[x, y]
            r = (r & ~1) | int(binary_data[data_index])  # embed in red channel
            data_index += 1
            if data_index < len(binary_data):
                g = (g & ~1) | int(binary_data[data_index])  # embed in green
                data_index += 1
            if data_index < len(binary_data):
                b = (b & ~1) | int(binary_data[data_index])  # embed in blue
                data_index += 1
            pixels[x, y] = (r, g, b)

    img.save(output_path)

def extract_data_from_image(image_path, length):
    img = Image.open(image_path)
    pixels = img.load()
    
    width, height = img.size
    bits = ''
    data_index = 0
    for y in range(height):
        for x in range(width):
            if data_index >= length:
                return bits
            r, g, b = pixels[x, y]
            bits += str(r & 1)
            data_index += 1
            if data_index >= length: break
            bits += str(g & 1)
            data_index += 1
            if data_index >= length: break
            bits += str(b & 1)
            data_index += 1
    return bits
