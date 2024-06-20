import os
import numpy as np
import cv2
input_folder = "./images"
output_folder = "./processed_images"
def process_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".jpeg"):
            filepath = os.path.join(input_folder, filename)
            frame = cv2.imread(filepath)
            
            if frame is None:
                continue
            
            # Resize frame with required image size
            frame_resized = cv2.resize(frame, (513, 513))
            
            # Pad smaller dimensions to mean value & multiply with 0.007843
            blob = cv2.dnn.blobFromImage(frame_resized, 0.007843, (513, 513), (127.5, 127.5, 127.5), swapRB=True)
            
            # Making numpy array of required shape
            blob = np.reshape(blob, (1, 513, 513, 3))
            
            # Storing to a raw file
            output_filepath = os.path.join(output_folder, os.path.splitext(filename)[0] + '.raw')
            blob.tofile(output_filepath)

# Example usage:

process_images(input_folder, output_folder)

