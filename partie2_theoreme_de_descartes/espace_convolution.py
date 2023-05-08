from PIL import Image
from numpy import asarray
import numpy as np
from tqdm import tqdm
import scipy.signal as sg

img = np.array(Image.open('essai box counting.png'))
img = img[:, :, 0]
img = img.astype(np.int16)

edge = np.array([[0, 1, -0], [1, -4, 1], [0, 1, 0]])
results = sg.convolve(img, edge, mode='same')
results[results > 255] = 255
results[results < 0] = 0

results = results.astype(np.uint8)

img = np.array(results)
from matplotlib import cm
im = Image.fromarray(np.uint8(cm.gist_earth(results)*255))
im.save('essai box counting convolution.png', 'png')