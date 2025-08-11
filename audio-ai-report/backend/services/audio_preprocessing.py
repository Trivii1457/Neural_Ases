from pydub import AudioSegment
import numpy as np

class AudioPreprocessor:
    def __init__(self, audio_file_path):
        self.audio_file_path = audio_file_path
        self.audio_segment = None

    def load_audio(self):
        self.audio_segment = AudioSegment.from_file(self.audio_file_path)

    def normalize_audio(self):
        if self.audio_segment is not None:
            self.audio_segment = self.audio_segment.apply_gain(-self.audio_segment.dBFS)

    def convert_to_mono(self):
        if self.audio_segment is not None:
            self.audio_segment = self.audio_segment.set_channels(1)

    def get_samples(self):
        if self.audio_segment is not None:
            return np.array(self.audio_segment.get_array_of_samples())

    def preprocess(self):
        self.load_audio()
        self.normalize_audio()
        self.convert_to_mono()
        return self.get_samples()