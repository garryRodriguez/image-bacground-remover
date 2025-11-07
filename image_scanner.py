import os
from rembg import remove
from PIL import Image, ImageFilter, ImageOps

def scan_and_clean(input_path, output_path):
    # Load image
    img = Image.open(input_path)
    img = ImageOps.autocontrast(img)
    img = img.filter(ImageFilter.SHARPEN)

    # Remove background → transparent PNG
    img = remove(img)

    # Convert to RGBA to handle transparency
    img = img.convert("RGBA")

    # Create pure white background
    white_bg = Image.new("RGBA", img.size, (255, 255, 255, 255))

    # Paste cleaned image onto the white background
    white_bg.paste(img, (0, 0), img)

    # Convert to RGB (no alpha channel)
    final_img = white_bg.convert("RGB")

    # Save to output file
    final_img.save(output_path)


# Directories
input_dir = '/Users/garry/Desktop/practice--files/python-image-scanner-background-remover/images/'
output_dir = '/Users/garry/Desktop/practice--files/python-image-scanner-background-remover/output/'

os.makedirs(output_dir, exist_ok=True)

# Loop through all images
for file in os.listdir(input_dir):
    if file.lower().endswith(('.png', '.jpg', '.jpeg')):
        input_file = os.path.join(input_dir, file)
        output_file = os.path.join(output_dir, f"cleaned_{file.split('.')[0]}.jpg")  
        # Saving as JPG (better for white background)

        print(f"Cleaning: {file}...")
        scan_and_clean(input_file, output_file)

print("Done cleaning all images!")