from keras.models import load_model
import os

class ModelLoader:
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = self.load_model()

    def load_model(self):
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"Model file not found at {self.model_path}")
        return load_model(self.model_path)

    def get_model(self):
        return self.model