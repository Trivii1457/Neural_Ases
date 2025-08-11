from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pandas as pd
import numpy as np
import os

class AudioModelTrainer:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.model = RandomForestClassifier()
    
    def load_data(self):
        if not os.path.exists(self.dataset_path):
            raise FileNotFoundError(f"Dataset not found at {self.dataset_path}")
        data = pd.read_csv(self.dataset_path)
        return data

    def preprocess_data(self, data):
        # Assuming the last column is the target variable
        X = data.iloc[:, :-1]
        y = data.iloc[:, -1]
        return X, y

    def train_model(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)
        print(classification_report(y_test, y_pred))

    def save_model(self, model_path):
        import joblib
        joblib.dump(self.model, model_path)

if __name__ == "__main__":
    trainer = AudioModelTrainer(dataset_path='path/to/your/dataset.csv')
    data = trainer.load_data()
    X, y = trainer.preprocess_data(data)
    trainer.train_model(X, y)
    trainer.save_model(model_path='path/to/save/your/model.pkl')