from PIL import Image
import os

# Assignment:
# Create a new folder called "processed" where all images from "raw" are stored in .png.
# They are all cropped to ratio 4:3 (landscape) (or 3:4 - portrait) and resized to be all the same size.

# Notice:
# 1. There are different extensions
# 2. They are all different sizes
# 3. We have portrait and landscape orientated images

# Steps
# 0. Create a new folder
# 1. Define portrait and landscape images
# 2. Figure out on which side you have to crop the image
# 3. Crop the image
# 4. Resize the image
# 5. Save it to your new folder with the new extension. That's it!

new_folder = '/Users/koendereus/Desktop/session2a-image/processed'
if not os.path.isdir(new_folder):
    os.mkdir(new_folder)

folder = '/Users/koendereus/Desktop/session2a-image/raw'
img_list = os.listdir(folder)
landscape_size = (400, 300)
portrait_size = (300, 400)

for img_filename in img_list:
    if img_filename == ".DS_Store":
        continue # skips loop iteration if filename is ".DS_Store"

    img_path = os.path.join(folder, img_filename)
    image = Image.open(img_path)

    if image.width > image.height: #landscape
        if image.width / image.height < 4 / 3: #crop height
            new_height = (3 * image.width) / 4
            reg = (0, 0, image.width, new_height)

        else: #crop width
            new_width = (4 * image.height) / 3
            reg = (0, 0, new_width, image.height)

        new_size = landscape_size

    else: #portrait
        if image.width / image.height < 3/4: #crop height
            new_height = (4 * image.width) / 3
            reg = (0, 0, image.width, new_height)

        else: #crop width
            new_width = (3 * image.height) / 4
            reg = (0, 0, new_width, image.height)

        new_size = portrait_size

    image_cropped = image.crop(reg)
    image_cropped_and_resized = image_cropped.resize(new_size)
    filename, extension = os.path.splitext(img_filename)
    outfile = filename + '.png'
    image_cropped_and_resized.save(os.path.join(new_folder, outfile))