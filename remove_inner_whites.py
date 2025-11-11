from PIL import Image, ImageFilter
import os

input_folder = "../examples/before/"
output_folder = "../examples/after/"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        im = Image.open(os.path.join(input_folder, filename)).convert("RGBA")
        alpha = im.split()[-1].filter(ImageFilter.MinFilter(3))
        im.putalpha(alpha)
        im.save(os.path.join(output_folder, filename))
        print(f"Processed {filename}")
