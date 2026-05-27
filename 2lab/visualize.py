import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as MplPolygon


def visualize(polygons, title="Polygons"):

    fig, ax = plt.subplots()

    for poly in polygons:

        patch = MplPolygon(
            poly,
            closed=True,
            fill=False
        )

        ax.add_patch(patch)

    ax.autoscale()

    ax.set_aspect('equal')

    plt.title(title)

    plt.grid(True)

    plt.show()
