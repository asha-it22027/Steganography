import time
from PIL import Image
import os
import sys

# Add current directory to path so we can import stego
sys.path.append(os.getcwd())

from stego.utils import encode_lsb, decode_lsb

def benchmark():
    img_size = (1920, 1280)
    img = Image.new('RGB', img_size, color='red')
    img_path = 'test_large.png'
    img.save(img_path)
    
    message = "Hello World"
    output_path = 'test_encoded.png'
    
    print("Encoding...")
    start = time.time()
    encode_lsb(img_path, message, output_path)
    print(f"Encoding took {time.time() - start:.4f}s")
    
    print("Decoding...")
    start = time.time()
    decoded = decode_lsb(output_path)
    end = time.time()
    print(f"Decoding took {end - start:.4f}s")
    print(f"Decoded message: '{decoded}'")
    
    # Clean up
    if os.path.exists(img_path): os.remove(img_path)
    if os.path.exists(output_path): os.remove(output_path)

if __name__ == "__main__":
    benchmark()
