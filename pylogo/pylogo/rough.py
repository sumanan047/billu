import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


fig, ax = plt.subplots()
rect = patches.Rectangle((1, 2), 1, 1, linewidth=1, edgecolor='black', facecolor='lightblue')
ax.add_patch(rect)
ax.set_xlim(0, 15)
ax.set_ylim(0, 15)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Single Rectangular Patch Example")

# Animate movement for 5 frames
for _ in range(5):
    dx, dy = np.random.uniform(-1, 1, 2)  # Random direction
    rect.set_xy(rect.get_xy() + np.array([dx, dy]))  # Update patch position
    plt.pause(0.5)  # Pause for 0.5 seconds to show animation

plt.show()
