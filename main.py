import os
import sys
import shutil
from PIL import Image

# Configuration
directory_to_search = None      # Directory to recursively search
target_directory_name = None             # Directory to match images inside
image_output_dir = os.getcwd() + "/__Collected_Images"        # Directory to copy matched images to
output_pdf_name = 'Grouped_Images.pdf'  # Output PDF name

# main.py images final Grouped_Images

if len(sys.argv) > 1:
    directory_to_search = os.getcwd() + '/' + sys.argv[1]
if len(sys.argv) > 2:
    target_directory_name = sys.argv[2]
if len(sys.argv) > 3:
    output_pdf_name = sys.argv[3] + '.pdf'
# if len(sys.argv) > 1:
#     directory_to_search = os.getcwd() + '/' + sys.argv[1]
#     target_directory_name = sys.argv[2]
#     output_pdf_name = sys.argv[3] + '.pdf'

# Create the output folder if it doesn't exist
if not os.path.exists(image_output_dir):
    os.makedirs(image_output_dir)

# Traverse the directory and collect images
def collect_images(root_dir, target_directory_name):
    for root, dirs, files in os.walk(root_dir):
        if os.path.basename(root) == target_directory_name:
            for file in files:
                if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                    src_path = os.path.join(root, file)
                    dest_path = os.path.join(image_output_dir, file)
                    shutil.copy(src_path, dest_path)
                    print(f"Copied: {src_path} -> {dest_path}")

# Create a PDF from collected images
def create_pdf_from_images(image_dir, pdf_name):
    image_files = [
        os.path.join(image_dir, file)
        for file in os.listdir(image_dir)
        if file.lower().endswith(('.png', '.jpg', '.jpeg'))
    ]
    image_files.sort()  # Optional: Sort images alphabetically
    if image_files:
        # Open the first image
        first_image = Image.open(image_files[0]).convert("RGB")
        other_images = [
            Image.open(img).convert("RGB") for img in image_files[1:]
        ]
        first_image.save(pdf_name, save_all=True, append_images=other_images)
        print(f"PDF created: {pdf_name}")
    else:
        print("No images found to create PDF.")


# Run the script
collect_images(directory_to_search, target_directory_name)
create_pdf_from_images(image_output_dir, output_pdf_name)