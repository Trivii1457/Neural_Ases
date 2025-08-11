from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import os

class AudioDataset:
    def __init__(self, audio_dir, labels_file):
        self.audio_dir = audio_dir
        self.labels_file = labels_file
        self.audio_files = []
        self.labels = []
        self.load_dataset()

    def load_dataset(self):
        if not os.path.exists(self.labels_file):
            raise FileNotFoundError(f"Labels file not found: {self.labels_file}")

        labels_df = pd.read_csv(self.labels_file)
        for index, row in labels_df.iterrows():
            audio_file = os.path.join(self.audio_dir, row['filename'])
            if os.path.exists(audio_file):
                self.audio_files.append(audio_file)
                self.labels.append(row['label'])
            else:
                print(f"Audio file not found: {audio_file}")

    def get_data(self):
        return train_test_split(self.audio_files, self.labels, test_size=0.2, random_state=42)

    def __len__(self):
        return len(self.audio_files)