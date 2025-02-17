import numpy as np
from sklearn.neighbors import NearestNeighbors  

# Mock dataset  
X = np.array([[0.9, 0.8], [0.95, 0.2], [0.3, 0.95]])  

knn = NearestNeighbors(n_neighbors=2, metric='euclidean')  
knn.fit(X)  

# Query  
query = np.array([[0.88, 0.15]])  
distances, indices = knn.kneighbors(query)  

print(f"Indices: {indices}, Distances: {distances}")  
