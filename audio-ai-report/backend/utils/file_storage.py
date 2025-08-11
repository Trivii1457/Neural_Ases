from pathlib import Path

class FileStorage:
    def __init__(self, base_directory):
        self.base_directory = Path(base_directory)
        self.audio_directory = self.base_directory / 'audio_files'
        self.audio_directory.mkdir(parents=True, exist_ok=True)

    def save_audio_file(self, audio_file):
        audio_path = self.audio_directory / audio_file.filename
        with open(audio_path, 'wb') as f:
            f.write(audio_file.read())
        return audio_path

    def get_audio_file_path(self, filename):
        return self.audio_directory / filename

    def delete_audio_file(self, filename):
        audio_path = self.get_audio_file_path(filename)
        if audio_path.exists():
            audio_path.unlink()
            return True
        return False

    def list_audio_files(self):
        return [f.name for f in self.audio_directory.iterdir() if f.is_file()]