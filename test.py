

import numpy as np
from PIL import Image
data = np.zeros([224,224,3], np.uint8)
im = Image.fromarray(data)

im.save("img.jpg")