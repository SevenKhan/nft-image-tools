# NFT Image Tools

Python and Bash tools to process NFT images in bulk.

## Features
- Clean white/halo edges of NFT images
- Make very light colors inside images transparent
- Add background colors (red, gradient, etc.)

## Usage
1. Place your NFT images in `examples/before/`
2. Run scripts from the `scripts/` folder
   - Python: `python3 scripts/remove_inner_whites.py`
   - Bash: `bash scripts/final_clean.sh`
3. Processed images will appear in `examples/after/` and `examples/after_red/`

## Example NFT Images

### Before processing
![Before 1](examples/before/sample1.png)
![Before 2](examples/before/sample2.png)

### After processing
![After 1](examples/after/sample1.png)
![After 2](examples/after/sample2.png)

### Demo GIF (optional)
![Demo](examples/demo.gif)

## License
MIT
