import numpy as np
import faiss

# Mock dataset
X = np.array([[0.9, 0.8], [0.95, 0.2], [0.3, 0.95]]).astype('float32')

# Set dimensions
dim = X.shape[1]

# Create a flat L2 index as a quantizer
quantizer = faiss.IndexFlatL2(dim)

# Create an IVF index with 2 clusters
index_ivf = faiss.IndexIVFFlat(quantizer, dim, 2)

# Train the index
index_ivf.train(X)

# Add vectors to index
index_ivf.add(X)

# Search for nearest neighbors
index_ivf.nprobe = 1  # Search within 1 cluster
query = np.array([[0.88, 0.15]], dtype='float32')
D, I = index_ivf.search(query, k=2)

print(f"IVF matches: {I}")  # Expected output: Indices of closest matches
