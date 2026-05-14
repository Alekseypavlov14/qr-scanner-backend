import cv2
import numpy as np


MEDIAN_KERNEL = 5
GAUSS_KERNEL = 3
SHARPEN_STRENGTH = 1.0
UPSCALE_FACTOR = 2


def remove_salt_pepper(image):
  return cv2.medianBlur(image, MEDIAN_KERNEL)


def reduce_gaussian_noise(image):
  return cv2.GaussianBlur(image, (GAUSS_KERNEL, GAUSS_KERNEL), 0)


def normalize_illumination(image):
  return cv2.equalizeHist(image)


def sharpen(image):
  kernel = np.array([
    [0, -1, 0],
    [-1, 5 + SHARPEN_STRENGTH, -1],
    [0, -1, 0]
  ], dtype=np.float32)

  return cv2.filter2D(image, -1, kernel)


def upscale(image):
  return cv2.resize(
    image,
    None,
    fx=UPSCALE_FACTOR,
    fy=UPSCALE_FACTOR,
    interpolation=cv2.INTER_CUBIC
  )


def restore(image):
  if image is None:
    raise ValueError("INVALID IMAGE")

  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  img = remove_salt_pepper(gray)
  img = reduce_gaussian_noise(img)
  img = normalize_illumination(img)
  img = sharpen(img)
  img = upscale(img)

  return img