import os
from PIL import Image

# Folders
INPUT_FOLDER = "images"
OUTPUT_FOLDER = "output"

# Make sure output folder exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def resize_image(input_path, output_path, width, height):
    """Resize a single image to the specified width and height."""
    with Image.open(input_path) as img:
        resized = img.resize((width, height))
        resized.save(output_path)
        print(f"✅ Saved resized image to {output_path}")

def main():
    print("🖼️  Image Resizer Tool")
    print("----------------------")
    width = int(input("Enter new width (px): "))
    height = int(input("Enter new height (px): "))

    # Process all images in the input folder
    for filename in os.listdir(INPUT_FOLDER):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            input_path = os.path.join(INPUT_FOLDER, filename)
            output_path = os.path.join(OUTPUT_FOLDER, f"resized_{filename}")
            resize_image(input_path, output_path, width, height)

    print("\n🎉 All images have been resized and saved to the 'output' folder.")

if __name__ == "__main__":
    main()
