import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set axis labels and limits
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])

def plot_vector(x, y, z, color, label):
    ax.scatter([x], [y], [z], color=color, s=50, label=label)
    ax.plot([0, x], [0, y], [0, z], color=color, linewidth=2)
    return np.array([x, y, z])

# Define vectors
v1 = plot_vector(1, 1, 0.9, 'blue', 'Sentence 1')
v2 = plot_vector(1, 0.8, 0.7, 'red', 'Sentence 2')
v3 = plot_vector(0.1, 0, 0.1, 'green', 'Sentence 3')
vp = plot_vector(1, 0.8, 0.8, 'black', "User's Prompt")

# Function to compute angle and plot it
def plot_angle(vp, vi, label_color, label_text):
    dot = np.dot(vp, vi)
    mag_vp = np.linalg.norm(vp)
    mag_vi = np.linalg.norm(vi)
    angle_rad = np.arccos(dot / (mag_vp * mag_vi))
    angle_deg = np.degrees(angle_rad)
    
    # Midpoint for annotation
    mid = (vp + vi) / 4
    ax.text(mid[0], mid[1], mid[2], f'{label_text}: {angle_deg:.1f}°', color=label_color)

    print(f'{label_text} (angle between User\'s Prompt and {label_color.title()} vector): {angle_deg:.2f}°')

# Compute angles
plot_angle(vp, v1, 'blue', 'θ1')
plot_angle(vp, v2, 'red', 'θ2')
plot_angle(vp, v3, 'green', 'θ3')

# Add legend
ax.legend()
plt.show()
