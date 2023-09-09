import cv2
import numpy as np

def transfer_colors(source_image, target_image):
  source_hist = cv2.calcHist([source_image], [0], None, [256], [0, 255])
  target_hist = cv2.calcHist([target_image], [0], None, [256], [0, 255])

  # Normalize os histogramas.
  source_hist = source_hist / np.sum(source_hist)
  target_hist = target_hist / np.sum(target_hist)

  # Crie uma nova imagem com as cores transferidas.
  new_image = np.zeros_like(source_image)
  for i in range(source_image.shape[0]):
    for j in range(source_image.shape[1]):
      pixel = source_image[i, j]
      new_pixel = np.argmax(target_hist * source_hist[pixel])
      new_image[i, j] = new_pixel

  return new_image