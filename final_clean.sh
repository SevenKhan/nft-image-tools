#!/bin/bash
# Script: apply red background to processed images
mkdir -p ../examples/after_red

for f in ../examples/after/*.png; do
    convert "$f" -background red -alpha remove -alpha off -trim +repage "../examples/after_red/$(basename "$f")"
done

echo "All images processed with red background."
