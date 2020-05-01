
import matplotlib.pyplot as plt
import numpy as np

from PIL import Image

# x - data matrix of shape (w, h, 3) corresponding to a single RGB image
def view_image(x):
    plt.imshow(Image.fromarray(np.uint8(np.transpose(x, axes=[1, 0, 2]) * 255)))

# y - data matrix of shape (w, h) corresponding to a single grayscale image
def view_mask(y):
    plt.imshow(Image.fromarray(np.uint8(np.transpose(y) * 255), 'L'))

# x - data matrix of shape (w, h, 3) corresponding to a single RGB image
# y - data matrix of shape (w, h) corresponding to a single grayscale image
def view_image_mask(x, y):
    plt.imshow(Image.fromarray(np.uint8(np.transpose(x, axes=[1, 0, 2]) * 255)))
    plt.figure()
    plt.imshow(Image.fromarray(np.uint8(np.transpose(y) * 255), 'L'))

def view_image_mask2(x, y, y_true):
    plt.imshow(Image.fromarray(np.uint8(np.transpose(x, axes=[1, 0, 2]) * 255)))
    plt.figure()
    plt.imshow(Image.fromarray(np.uint8(np.transpose(y) * 255), 'L'))
    plt.figure()
    plt.imshow(Image.fromarray(np.uint8(np.transpose(y_true) * 255), 'L'))