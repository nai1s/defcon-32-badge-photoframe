from PIL import Image
import os
import argparse

def resize_images(input_folder, output_folder, size=(320, 240)):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.png')
            
            try:
                # Open an image file
                with Image.open(input_path) as img:
                    # Resize image
                    img = img.resize(size)
                    # Save as PNG
                    img.save(output_path, format='PNG')
                    print(f"Resized and saved {filename} to {output_path}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Resize images in a folder to 320x240 and save them as PNG files.')
    parser.add_argument('input_folder', type=str, help='Path to the input folder containing images.')
    parser.add_argument('output_folder', type=str, help='Path to the output folder where resized images will be saved.')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Call the function to resize images
    resize_images(args.input_folder, args.output_folder)

if __name__ == "__main__":
    main()