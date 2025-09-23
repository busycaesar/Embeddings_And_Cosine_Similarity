import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set axis labels
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

# Set limits for better visibility
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])

# Sentence 1

## Target point coordinates
x_end, y_end, z_end = 1, 0.8, 0.9

## Plot the point
ax.scatter([x_end], [y_end], [z_end], color='blue', s=50, label='Sentence 1')

## Plot a line from origin to the point
ax.plot([0, x_end], [0, y_end], [0, z_end], color='blue', linewidth=2)

# Sentence 2

## Target point coordinates
x_end, y_end, z_end = 0.9, 0.9, 1

## Plot the point
ax.scatter([x_end], [y_end], [z_end], color='red', s=50, label='Sentence 2')

## Plot a line from origin to the point
ax.plot([0, x_end], [0, y_end], [0, z_end], color='red', linewidth=2)

# Sentence 3

## Target point coordinates
x_end, y_end, z_end = 0, 0.1, 0.1

## Plot the point
ax.scatter([x_end], [y_end], [z_end], color='green', s=50, label='Sentence 3')

## Plot a line from origin to the point
ax.plot([0, x_end], [0, y_end], [0, z_end], color='green', linewidth=2)

# User's Prompt

## Target point coordinates
x_end, y_end, z_end = 1, 1, 0.7

## Plot the point
ax.scatter([x_end], [y_end], [z_end], color='black', s=50, label='User''s Prompt')

## Plot a line from origin to the point
ax.plot([0, x_end], [0, y_end], [0, z_end], color='black', linewidth=2)

# Add legend
ax.legend()

# Show plot
plt.show()
