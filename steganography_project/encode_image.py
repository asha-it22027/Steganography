from PIL import Image
from stego.utils import encode_lsb

input_path = r"C:\Users\ashra\Downloads\sakura"
output_path = "stego/static/stego/encoded_image.png"
message = "🌸 Sakura - The beauty of life is as fleeting as cherry blossoms."

encode_lsb(input_path, message, output_path)