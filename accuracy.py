import cv2
import numpy as np
import os 

def calculate_accuracy(recognizer, test_path, known_IDs):
  """
  Calculates the accuracy of the face recognition model.

  Args:
      recognizer: The trained face recognizer object.
      test_path: Path to the folder containing testing images.
      known_IDs: List of known IDs corresponding to the testing images.

  Returns:
      A tuple containing the following:
          - Total number of test images
          - Number of correctly recognized images
          - Accuracy percentage (float)
  """

  total_tests = 0
  correct = 0

  for filename in os.listdir(test_path):
    if filename.endswith(".jpg") or filename.endswith(".jng"):  # Handle common image formats
      img_path = os.path.join(test_path, filename)
      img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

      (predicted_ID, confidence) = recognizer.predict(img)
      total_tests += 1

      if predicted_ID == known_IDs[filename]:  # Use filename as index
        correct += 1

  accuracy = (correct / total_tests) * 100
  return total_tests, correct, accuracy


# Example usage
test_path = "datasets"
known_IDs = ["name1", "name2", ...]  # Replace with actual IDs from testing images

total_tests, correct, accuracy = calculate_accuracy(recognizer, test_path, known_IDs)
print(f"Total tests: {total_tests}")
print(f"Correct predictions: {correct}")
print(f"Accuracy: {accuracy:.2f}%")