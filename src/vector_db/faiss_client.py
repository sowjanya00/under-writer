import faiss
import numpy as np

class FaissClient:
    def __init__(self, dimension):
        self.index = faiss.IndexFlatL2(dimension)

    def add_vectors(self, vectors):
        self.index.add(np.array(vectors).astype('float32'))

    def search_vectors(self, query_vector, k=5):
        distances, indices = self.index.search(np.array([query_vector]).astype('float32'), k)
        return distances, indices