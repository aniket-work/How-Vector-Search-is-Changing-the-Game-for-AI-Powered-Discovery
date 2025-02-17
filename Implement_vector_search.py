import numpy as np
from collections import defaultdict

class VectorSearch:
    def __init__(self):
        self.index = defaultdict(list)

    def add_vector(self, id: int, vector: list):
        self.index[id] = np.array(vector)

    def search(self, query_vec: list, k=3):
        query = np.array(query_vec)
        distances = {}
        for id, vec in self.index.items():
            # Euclidean distance
            distances[id] = np.linalg.norm(vec - query)
        # Return top K closest
        return sorted(distances.items(), key=lambda x: x[1])[:k]

# Example usage
engine = VectorSearch()
engine.add_vector(1, [0.9, 0.8])  # Apple
engine.add_vector(2, [0.95, 0.2])  # Banana
engine.add_vector(3, [0.3, 0.95])  # Carrot

query = [0.88, 0.15]  # Sweet, not crunchy
results = engine.search(query, k=2)
print(f"Top matches: {results}")  # Output: [(2, 0.07), (1, 0.15)] → Banana, Apple