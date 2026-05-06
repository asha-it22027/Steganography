from PIL import Image
import os
from stego.utils import encode_lsb, decode_lsb

def test_steganography():
    test_message = "🌸 Sakura - The beauty of life is as fleeting as cherry blossoms." + "###END###"
    input_img_path = "test_input.png"
    output_img_path = "test_output.png"
    
    # Create a dummy image
    img = Image.new('RGB', (200, 200), color=(73, 109, 137))
    img.save(input_img_path)
    
    print(f"Testing with message: {test_message}")
    
    try:
        encode_lsb(input_img_path, test_message, output_img_path)
        decoded = decode_lsb(output_img_path)
        
        expected = test_message.replace("###END###", "")
        print(f"Decoded message: {decoded}")
        
        if decoded == expected:
            print("SUCCESS: Message decoded correctly!")
        else:
            print(f"FAILURE: Expected '{expected}', but got '{decoded}'")
            
    finally:
        if os.path.exists(input_img_path):
            os.remove(input_img_path)
        if os.path.exists(output_img_path):
            os.remove(output_img_path)

if __name__ == "__main__":
    test_steganography()
