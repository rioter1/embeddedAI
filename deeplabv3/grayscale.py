import os
import numpy as np
import cv2

def process_raw_files(preprocessed_folder, grayscale_folder, original_images_folder):
    if not os.path.exists(grayscale_folder):
        os.makedirs(grayscale_folder)

    for filename in os.listdir(preprocessed_folder):
        if filename.endswith(".raw"):
            filepath = os.path.join(preprocessed_folder, filename)
            arr = np.fromfile(filepath, dtype="float32")
            arr = np.reshape(arr, (1, 513, 513, 3))  # Ensure it matches the shape used in saving

            # Extract the segment (This might need adjustment based on actual requirements)
            segment = arr[0, 342:, 342:, 0]  # Assuming the segment is in the first channel

            # Mark certain values for processing
            arr[arr == 15] = 255

            # Read the original image (assumes it has the same name but with .jpg extension)
            original_image_name = filename.replace('.raw', '.jpg')
            original_image_path = os.path.join(original_images_folder, original_image_name)
            original_img = cv2.imread(original_image_path)

            if original_img is None:
                continue

            # Resize the segment to match the original image dimensions
            arr2 = cv2.resize(segment, (original_img.shape[1], original_img.shape[0]))

            # Process the original image based on the segment
            for i in range(arr2.shape[0]):
                for j in range(arr2.shape[1]):
                    if arr2[i][j] != 255:
                        original_img[i][j] = [original_img[i][j][0]] * 3

            # Save the processed image
            output_filepath = os.path.join(grayscale_folder, original_image_name)
            cv2.imwrite(output_filepath, original_img)

# Example usage:
preprocessed_folder = './processed_images'
grayscale_folder = './grayscale'
original_images_folder = './images'
process_raw_files(preprocessed_folder, grayscale_folder, original_images_folder)

