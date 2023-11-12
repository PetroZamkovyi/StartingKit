#!/usr/bin/python3

from PIL import Image
import os

# Input and output folders
input_folder = 'images'
output_folder = '/opt/icons/'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Iterate through each file in the input folder
for filename in os.listdir(input_folder):
    input_path = os.path.join(input_folder, filename)
    print(filename)

    # Check if the file is an image
    if filename != ".DS_Store":

        # Open the image
        print(2)
        with Image.open(input_path) as img:
            # Convert the image to RGB mode.
            img = img.convert('RGB')

            # Rotate the image 90° clockwise
            img = img.rotate(270)

            # Resize the image from 192x192 to 128x128
            img = img.resize((128, 128))

            # Create the output filename
            output_filename = os.path.splitext(filename)[0] + '_edited'

            # Save the image to the output folder
            output_path = os.path.join(output_folder, output_filename)
            img.save(output_path, "JPEG")

print("Operation completed successfully.")
