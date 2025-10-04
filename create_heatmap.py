import matplotlib.pyplot as plt
import matplotlib.axes as axes
import numpy as np
from skimage import io, transform
import matplotlib
import matplotlib as mpl
import processdata

def create_heatmap():
    data = np.zeros((80, 80)) # do not change
    
    datalist = processdata.create_data_for_heatmap()

    for point in datalist:
        data[point[0], point[1]] += 1

   # Create colormap mapping using matplotliba
    cmap = plt.cm.RdYlGn # pyright: ignore[reportAttributeAccessIssue]
    norm = mpl.colors.Normalize(vmin=data.min(), vmax=data.max()) # pyright: ignore[reportAttributeAccessIssue]
    
    # Apply colormap to get RGBA image
    rgba_data = cmap(norm(data))
    
    # Resize from 80x80 to 800x800 using skimage
    resized_data = transform.resize(rgba_data, (800, 800), order=0, preserve_range=True)
    
    rgb_data = (resized_data[:, :, :3] * 255).astype(np.uint8) # pyright: ignore[reportAttributeAccessIssue]

    io.imsave("hack-demo-61n/static/figs/test.png", rgb_data)


if __name__ == "__main__":
    create_heatmap()