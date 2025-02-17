import numpy as np

# Mock CLIP-like embeddings  
text_embedding = np.array([0.4, 0.6], dtype=np.float32)  
image_embedding = np.array([0.38, 0.58], dtype=np.float32)  

# Normalize vectors before concatenation  
text_embedding /= np.linalg.norm(text_embedding)  
image_embedding /= np.linalg.norm(image_embedding)  

# Concatenate and normalize  
multimodal_vec = np.concatenate([text_embedding, image_embedding])  

# Multimodal Index Class  
class MultimodalIndex:  
    def __init__(self):  
        self.texts = []  
        self.images = []  

    def add(self, text_vec, image_vec):  
        self.texts.append(text_vec)  
        self.images.append(image_vec)  

    def search(self, query_vec, alpha=0.5):  
        scores = [alpha * np.dot(query_vec, t) + (1-alpha) * np.dot(query_vec, i)  
                  for t, i in zip(self.texts, self.images)]  
        return sorted(enumerate(scores), key=lambda x: -x[1])  

# Example usage  
index = MultimodalIndex()  
index.add(text_embedding, image_embedding)  

query_embedding = np.array([0.5, 0.5, 0.5, 0.5], dtype=np.float32)  
results = index.search(query_embedding)  
print(f"Multimodal Search Results: {results}")  
