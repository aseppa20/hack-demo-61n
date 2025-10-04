import matplotlib.pyplot as plt
import matplotlib.axes as axes
import numpy as np

import matplotlib
import matplotlib as mpl

def create_heatmap():
    data = np.zeros((80, 80))
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


    fig, ax = plt.subplots(figsize=(800/300, 800/300), dpi=300)
    ax.axis('off')
    #ax.set_axis_off()
    #if __name__ == "__main__":
    im = ax.imshow(data, cmap="spring")


    # Loop over data dimensions and create text annotations.
    fig.tight_layout()
    # plt.figure(figsize=(800/300, 800/300), dpi=300)
    plt.savefig("static/figs/test.png", transparent=True, bbox_inches=0)
    #plt.show()

if __name__ == "__main__":
    create_heatmap()