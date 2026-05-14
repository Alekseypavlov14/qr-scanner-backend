import numpy as np
import cv2


def get_image_from_formdata(file_storage):
  file_bytes = np.frombuffer(file_storage.read(), np.uint8)
  img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
  
  return img
