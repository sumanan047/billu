import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.patches import Rectangle


# num_points = 100
# x = np.random.rand(num_points)
# y = np.random.rand(num_points)

# polygon = Polygon(np.column_stack((x, y)), closed=True)
# create a 100 rectangles at random positions
fig, ax = plt.subplots()
for i in range(100):
    x_min = 0.0
    x_max = 10.0
    y_min = 0.0
    y_max = 10.0

    x = np.random.uniform(x_min, x_max)
    y = np.random.uniform(y_min, y_max)
    rect = Rectangle((x, y), 1, 1)
    ax.add_patch(rect)

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
plt.show()