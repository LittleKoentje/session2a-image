from PIL import Image
from PIL import ImageFilter
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
new_folder = '/Users/koendereus/Desktop/session2a-image/processed'
os.mkdir(new_folder)

# 1. Define portrait and landscape images
img_landscape = []
img_portrait = []

folder = '/Users/koendereus/Desktop/session2a-image/raw'
img_list = os.listdir(folder)
print(img_list)

for img_filename in img_list:
    if img_filename == ".DS_Store":
        continue # skips loop iteration if filename is ".DS_Store"

    img_path = os.path.join(folder, img_filename)
    image = Image.open(img_path)
    # print(image, img_path)
    width = image.width
    height = image.height
    if width > height:
         img_landscape.append(img_filename)
    else:
         img_portrait.append(img_filename)

print(img_landscape)
print(img_portrait)

# 2. Figure out on which side you have to crop the image
# landscape = width 4/3 of height, so if more than 4/3, crop width, if less than 4/3 crop height
img_landscape_crop_width = []
img_landscape_crop_height = []
img_portrait_crop_width = []
img_portrait_crop_height = []

for img_filename in img_landscape:
    img_path = os.path.join(folder, img_filename)
    image = Image.open(img_path)
    # print(image, img_path)
    width = image.width
    height = image.height
    if width / height < 4/3:
         img_landscape_crop_height.append(img_filename)
    else:
         img_landscape_crop_width.append(img_filename)

print(img_landscape_crop_height)
print(img_landscape_crop_width)

# portrait = width 3/4 of height, so if more than 3/4, crop width, if less than 3/4 crop height
for img_filename in img_portrait:
    img_path = os.path.join(folder, img_filename)
    image = Image.open(img_path)
    # print(image, img_path)
    width = image.width
    height = image.height
    if width / height < 3/4:
         img_portrait_crop_height.append(img_filename)
    else:
         img_portrait_crop_width.append(img_filename)

print(img_portrait_crop_height)
print(img_portrait_crop_width)

# 3. Crop the image
cropped_folder = '/Users/koendereus/Desktop/session2a-image/cropped'
os.mkdir(cropped_folder)

for img_filename in img_landscape_crop_width:
    img_path = os.path.join(folder, img_filename)
    image = Image.open(img_path)
    # Create a 4:3 ratio image
    new_width = (4 * image.height) / 3
    reg = (0, 0, new_width, image.height)
    image_cropped = image.crop(reg)
    image_cropped.save(os.path.join(cropped_folder, img_filename))

for img_filename in img_landscape_crop_height:
    img_path = os.path.join(folder, img_filename)
    image = Image.open(img_path)
    # Create a 4:3 ratio image
    new_height = (3 * image.width) / 4
    reg = (0, 0, image.width, new_height)
    image_cropped = image.crop(reg)
    image_cropped.save(os.path.join(cropped_folder, img_filename))

for img_filename in img_portrait_crop_width:
    img_path = os.path.join(folder, img_filename)
    image = Image.open(img_path)
    # Create a 3:4 ratio image
    new_width = (3 * image.height) / 4
    reg = (0, 0, new_width, image.height)
    image_cropped = image.crop(reg)
    image_cropped.save(os.path.join(cropped_folder, img_filename))

for img_filename in img_portrait_crop_height:
    img_path = os.path.join(folder, img_filename)
    image = Image.open(img_path)
    # Create a 3:4 ratio image
    new_height = (4 * image.width) / 3
    reg = (0, 0, image.width, new_height)
    image_cropped = image.crop(reg)
    image_cropped.save(os.path.join(cropped_folder, img_filename))

# 4. Resize the image
resized_folder = '/Users/koendereus/Desktop/session2a-image/resized'
os.mkdir(resized_folder)

landscape_size = (400, 300)
portrait_size = (300, 400)

for img_filename in img_landscape:
    img_path = os.path.join(cropped_folder, img_filename)
    image = Image.open(img_path)
    # Resize image
    image_resized = image.resize(landscape_size)
    image_resized.save(os.path.join(resized_folder, img_filename))

for img_filename in img_portrait:
    img_path = os.path.join(cropped_folder, img_filename)
    image = Image.open(img_path)
    # Resize image
    image_resized = image.resize(portrait_size)
    image_resized.save(os.path.join(resized_folder, img_filename))

# 5. Save it to your new folder with the new extension. That's it!
for img_filename in img_list:
    if img_filename == ".DS_Store":
        continue # skips loop iteration if filename is ".DS_Store"

    filename, extension = os.path.splitext(img_filename)
    outfile = filename + '.png'
    img_path = os.path.join(resized_folder, img_filename)
    img_open = Image.open(img_path)
    img_open.save(os.path.join(new_folder, outfile))