from pinecone import Pinecone

class PineconeClient:
    def __init__(self, api_key: str, environment: str):
        self.api_key = api_key
        self.environment = environment
        self.index = None
        self.initialize()

    def initialize(self):
        Pinecone.init(api_key=self.api_key, environment=self.environment)

    def create_index(self, index_name: str, dimension: int):
        if index_name not in Pinecone.list_indexes():
            Pinecone.create_index(index_name, dimension=dimension)
        self.index = Pinecone.Index(index_name)

    def upsert_vectors(self, vectors: list):
        if self.index is not None:
            self.index.upsert(vectors)

    def query_vectors(self, vector: list, top_k: int = 10):
        if self.index is not None:
            return self.index.query(vector, top_k=top_k)

    def delete_index(self, index_name: str):
        if index_name in Pinecone.list_indexes():
            Pinecone.delete_index(index_name)