from PIL import Image

def encode_lsb(image_path, message, output_path):
    img = Image.open(image_path).convert('RGB')
    pixels = list(img.getdata())
    
    message += "###END###"
    binary = ''
    for char in message:
        binary += format(ord(char), '08b')
    
    if len(binary) > len(pixels) * 3:
        raise ValueError("Message too long!")
    
    new_pixels = []
    bit_index = 0
    for r, g, b in pixels:
        if bit_index < len(binary):
            r = (r & 0xFE) | int(binary[bit_index])
            bit_index += 1
        if bit_index < len(binary):
            g = (g & 0xFE) | int(binary[bit_index])
            bit_index += 1
        if bit_index < len(binary):
            b = (b & 0xFE) | int(binary[bit_index])
            bit_index += 1
        new_pixels.append((r, g, b))
    
    new_img = Image.new('RGB', img.size)
    new_img.putdata(new_pixels)
    new_img.save(output_path, 'PNG')
    print("Encoded successfully!")

def decode_lsb(image_path):
    img = Image.open(image_path).convert('RGB')
    pixels = list(img.getdata())
    
    binary = ''
    text = ''
    for r, g, b in pixels:
        binary += str(r & 1)
        binary += str(g & 1)
        binary += str(b & 1)
        
        while len(binary) >= 8:
            byte = binary[:8]
            binary = binary[8:]
            char = chr(int(byte, 2))
            text += char
            if text.endswith('###END###'):
                return text[:-9]
    
    return ''