import numpy as np
import hnswlib

# Mock dataset
X = np.array([[0.9, 0.8], [0.95, 0.2], [0.3, 0.95]], dtype=np.float32)

# Build index
dim = X.shape[1]
index = hnswlib.Index(space='l2', dim=dim)
index.init_index(max_elements=1000, ef_construction=200, M=16)
index.add_items(X, np.arange(len(X)))  # Need to provide labels

# Search
query = np.array([[0.88, 0.15]], dtype=np.float32)
labels, distances = index.knn_query(query, k=2)

print(f"HNSW matches: {labels}")
