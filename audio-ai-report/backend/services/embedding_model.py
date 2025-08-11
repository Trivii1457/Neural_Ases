from sklearn.preprocessing import LabelEncoder
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class EmbeddingModel:
    def __init__(self, model):
        self.model = model
        self.label_encoder = LabelEncoder()

    def generate_embeddings(self, text):
        # Convert text to embeddings using the provided model
        embeddings = self.model.encode(text)
        return embeddings

    def compute_similarity(self, embedding1, embedding2):
        # Compute cosine similarity between two embeddings
        similarity = cosine_similarity([embedding1], [embedding2])
        return similarity[0][0]

    def encode_labels(self, labels):
        # Encode labels to numerical values
        return self.label_encoder.fit_transform(labels)

    def decode_labels(self, encoded_labels):
        # Decode numerical values back to original labels
        return self.label_encoder.inverse_transform(encoded_labels)