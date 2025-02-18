import numpy as np
import matplotlib.pyplot as plt

# Define the query customer (center point)
query_customer = np.array([0, 0])

# Define nearest customers (customers with similar preferences)
nearest_customers = np.array([[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]])

# Define non-nearest customers (different buying behavior)
other_customers = np.array([[3, 3], [3, -3], [-3, -3], [-3, 3]])

# Create the plot
fig, ax = plt.subplots(figsize=(6, 6))

# Plot the query customer (blue dot)
ax.scatter(query_customer[0], query_customer[1], color='navy', s=100, label="Query Customer", zorder=3)

# Plot nearest customers (green-filled circles)
ax.scatter(nearest_customers[:, 0], nearest_customers[:, 1], color='limegreen', s=200, edgecolors='black', zorder=2, label="Similar Customers")

# Plot other customers (white empty circles)
ax.scatter(other_customers[:, 0], other_customers[:, 1], color='white', s=200, edgecolors='green', linewidth=2, zorder=1, label="Other Customers")

# Draw arrows from query customer to nearest customers
for customer in nearest_customers:
    ax.arrow(query_customer[0], query_customer[1], customer[0] * 0.8, customer[1] * 0.8,
             head_width=0.15, head_length=0.2, fc='navy', ec='navy')

# Formatting the plot
ax.axhline(0, color='black', linewidth=1)  # X-axis
ax.axvline(0, color='black', linewidth=1)  # Y-axis
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_title("kNN Search for Customer Segmentation", fontsize=12)
ax.legend()
plt.show()
