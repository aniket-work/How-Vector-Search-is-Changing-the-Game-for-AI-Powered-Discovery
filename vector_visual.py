import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Sample data
categories = ['Cars', 'Bikes', 'Trucks']
subcategories = {
    'Cars': ['Sedan', 'SUV', 'Convertible'],
    'Bikes': ['Mountain', 'Road', 'Hybrid'],
    'Trucks': ['Pickup', 'Semi', 'Box']
}

# Generating random data points for each subcategory
np.random.seed(0)
data = {
    'Cars': {sub: np.random.rand(10, 3) for sub in subcategories['Cars']},
    'Bikes': {sub: np.random.rand(10, 3) for sub in subcategories['Bikes']},
    'Trucks': {sub: np.random.rand(10, 3) for sub in subcategories['Trucks']}
}

# Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Colors for each category
colors = {
    'Cars': 'blue',
    'Bikes': 'green',
    'Trucks': 'red'
}

# Plotting each category
for category, subcats in subcategories.items():
    for subcat, points in data[category].items():
        ax.scatter(points[:, 0], points[:, 1], points[:, 2], c=colors[category], label=f'{category}: {subcat}', alpha=0.6)

# Annotating the plot
for category, subcats in subcategories.items():
    for subcat in subcats:
        center = np.mean(data[category][subcat], axis=0)
        ax.text(center[0], center[1], center[2], f'{subcat}', color=colors[category], fontsize=9, fontweight='bold')

# Labeling the axes
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D Scatter Plot of Vehicles')
ax.legend()

# Show plot
plt.show()
