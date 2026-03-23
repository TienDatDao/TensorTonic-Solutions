import numpy as np

def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    image = np.array(image)
    R = image[:, :, 0]
    G = image[:, :, 1]
    B = image[:, :, 2]
    ans = 0.299 * R + 0.587 * G + 0.114 * B
    return ans.tolist()

