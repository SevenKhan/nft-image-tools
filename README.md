# NFT Image Tools

This repository provides easy-to-use Python and Bash scripts to process NFT images in bulk. 
With these tools, you can clean up white edges, enhance transparency, and add custom backgrounds 
to your NFT artwork, making them ready for professional presentation or marketplaces. 
Before-and-after examples are included to clearly demonstrate the effect of the scripts.

## Features
- Clean white/halo edges of NFT images
- Make very light colors inside images transparent
- Add background colors (red, gradient, etc.)

## Usage
1. Place your NFT images in `examples/before/`
2. Run scripts from the `scripts/` folder:
   - Python: `python3 scripts/remove_inner_whites.py`
   - Bash: `bash scripts/final_clean.sh`
3. Processed images will appear in `examples/after/` and `examples/after_red/`

## Example NFT Images

### Before processing
Here are some examples of the original NFT images:

![Before 1](examples/before/sample1.png)
![Before 2](examples/before/sample2.png)

### After processing
Here are the results after running the scripts:

![After 1](examples/after/sample1.png)
![After 2](examples/after/sample2.png)

### Demo GIF
You can also show all processed images in one GIF:

![Demo](examples/demo.gif)

## License
MIT
