import os
import shutil
import random

# Set the root folder containing property folders
root_folder = "resized cards"

# Define the ratio of images to be used for testing
test_ratio = 0.2  # 20% of images will be used for testing

# Function to split images into test and train sets
def split_images(property_folder):
    # Create test and train folders if they don't exist already
    test_folder = os.path.join(property_folder, "test")
    train_folder = os.path.join(property_folder, "train")
    os.makedirs(test_folder, exist_ok=True)
    os.makedirs(train_folder, exist_ok=True)

    # Get list of images in the property folder
    images = os.listdir(property_folder)

    # Calculate the number of images for testing
    num_test_images = int(len(images) * test_ratio)

    # Randomly select images for testing
    test_images = random.sample(images, num_test_images)

    # Move the selected test images to the test folder
    for image in test_images:
        src = os.path.join(property_folder, image)
        dst = os.path.join(test_folder, image)
        shutil.move(src, dst)

    # Move the remaining images to the train folder
    for image in os.listdir(property_folder):
        src = os.path.join(property_folder, image)
        dst = os.path.join(train_folder, image)
        shutil.move(src, dst)

# Iterate through each property folder
for property_folder in os.listdir(root_folder):
    property_folder_path = os.path.join(root_folder, property_folder)

    # Check if the item is a directory
    if os.path.isdir(property_folder_path):
        # Split images in the property folder into test and train sets
        split_images(property_folder_path)

print("Images successfully split into test and train sets.")
