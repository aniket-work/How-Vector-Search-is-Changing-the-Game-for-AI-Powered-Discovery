import matplotlib.pyplot as plt
import numpy as np

# Mock embeddings: [sweetness, crunchiness]
fruits = {
    "Apple": [0.9, 0.8],
    "Banana": [0.95, 0.2],
    "Carrot": [0.3, 0.95],
    "Grapes": [0.85, 0.1]
}

# Plotting
plt.figure(figsize=(8, 6))
for fruit, vec in fruits.items():
    plt.scatter(vec[0], vec[1], label=fruit)
plt.xlabel("Sweetness →"), plt.ylabel("Crunchiness →")
plt.title("Fruit Vector Space")
plt.legend()
plt.grid(True)
plt.show()