import os
import cv2

# Function to resize images in nested folders
def resize_images_in_nested_folders(input_folder, output_folder, target_size):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through each item in the input folder
    for item in os.listdir(input_folder):
        item_path = os.path.join(input_folder, item)

        if os.path.isdir(item_path):  # If item is a directory, recursively call the function
            output_subfolder = os.path.join(output_folder, item)
            resize_images_in_nested_folders(item_path, output_subfolder, target_size)

        elif item.endswith(('.jpg', '.jpeg', '.png', '.bmp')):  # If item is an image file
            # Read the image
            image = cv2.imread(item_path)

            # Resize the image
            resized_image = cv2.resize(image, target_size)

            # Save the resized image to the output folder
            output_path = os.path.join(output_folder, item)
            cv2.imwrite(output_path, resized_image)

# Set input and output folders
input_root_folder = "custom_data"
output_root_folder = "resized custom data"
target_size = (1500, 1000)  # Set the target size for resizing

# Call the function to resize images in nested folders
resize_images_in_nested_folders(input_root_folder, output_root_folder, target_size)

print("Resizing complete.")
