import matplotlib.pyplot as plt
import matplotlib.axes as axes
import numpy as np
from skimage import io, transform
import matplotlib
import matplotlib as mpl

def create_heatmap():
    data = np.zeros((80, 80)) # do not change
    data [1, 0] += 10
    data [2, 0] += 10
    data [3, 0] += 10
    data [4, 0] += 10
    data [5, 0] += 10
    data [6, 0] += 10
    data [7, 0] += 10
    data [8, 0] += 10
    data [9, 0] += 10
    data [0,0] += 10
    data [0,1] += 10
    data [0,2] += 10
    data [0,3] += 10
    data [0,4] += 10
    data [0,5] += 10
    data [0,6] += 10
    data [0,7] += 10
    data [0,8] += 10
    data [0,9] += 10

    #Helsinki
    data [67, 47] += 10
    data [68, 48] += 10
    data [69, 49] += 10
    data [70, 50] += 10
    data [71, 51] += 10
    data [72, 52] += 10

    #Nurmijärvi
    data[14, 37] += 10
    data[20, 40] += 10
    data[12, 35] += 10

    #Järvenpää
    data[12, 64] += 10
    data[17, 70] += 10

    #Espoo/Kauniainen
    data[60, 25] += 10
    data[68, 30] += 10

    #Vantaa
    data[42, 50] += 10
    data[49, 60] += 10

   # Create colormap mapping using matplotliba
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