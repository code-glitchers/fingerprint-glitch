import cv2
import os
import numpy as np

def preprocess_fingerprint(image):
    # Your preprocessing steps here (similar to previous examples)
    preprocessed_image = image  # Placeholder, replace this with actual preprocessing
    return preprocessed_image

def match_fingerprint(template, target_image):
    # Get dimensions of the target image
    height, width = target_image.shape
    
    # Resize the template using numpy
    template = cv2.resize(template, (width, height))
    
    # Perform template matching using OpenCV's matchTemplate function
    result = cv2.matchTemplate(target_image, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    
    return max_val

def main():
    # Load the fingerprint image to be matched
    target_image_path = 'img0026.jpg'
    target_image = cv2.imread(target_image_path, cv2.IMREAD_GRAYSCALE)
    preprocessed_target = preprocess_fingerprint(target_image)
    
    # Iterate through fingerprint images in the folder
    folder_path = 'fingerprint/'
    template_filenames = os.listdir(folder_path)
    
    for template_filename in template_filenames:
        template_path = os.path.join(folder_path, template_filename)
        template_image = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
        preprocessed_template = preprocess_fingerprint(template_image)
        
        match_score = match_fingerprint(preprocessed_template, preprocessed_target)
        
        print(f"Match score with {template_filename}: {match_score}")

if __name__ == "__main__":
    main()
