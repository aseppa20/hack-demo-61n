import matplotlib.pyplot as plt
import matplotlib.axes as axes
import numpy as np
from skimage import io, transform
import matplotlib
import matplotlib as mpl

def create_heatmap():
    data = np.zeros((80, 80)) # do not change
    data [0, 0] += 8
    data [1, 0] += 8
    data [0, 2] += 8
    data [1, 2] += 8
    data [2, 2] += 4
    data [3, 2] += 4
    data [4, 3] += 4
    data [4, 4] += 4
    data [18,12] += 4
    data [18,13] += 4

   # Create colormap mapping using matplotlib
    cmap = plt.cm.spring
    norm = mpl.colors.Normalize(vmin=data.min(), vmax=data.max())
    
    # Apply colormap to get RGBA image
    rgba_data = cmap(norm(data))
    
    # Resize from 80x80 to 800x800 using skimage
    resized_data = transform.resize(rgba_data, (800, 800), order=0, preserve_range=True)
    
    rgb_data = (resized_data[:, :, :3] * 255).astype(np.uint8)

    io.imsave("hack-demo-61n/static/figs/test.png", rgb_data)


if __name__ == "__main__":
    create_heatmap()