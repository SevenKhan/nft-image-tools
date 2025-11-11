# remove_inner_whites.py
# This script removes inner white/halo edges from PNG images

from PIL import Image, ImageFilter
import os

input_dir = "../examples/before"
output_dir = "../examples/after"

os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.lower().endswith(".png"):
        filepath = os.path.join(input_dir, filename)
        im = Image.open(filepath).convert("RGBA")

        # Split alpha channel and slightly smooth
        alpha = im.split()[-1].filter(ImageFilter.MinFilter(3))
        im.putalpha(alpha)

        output_path = os.path.join(output_dir, filename)
        im.save(output_path)

print("All images processed and saved to 'examples/after/'")
