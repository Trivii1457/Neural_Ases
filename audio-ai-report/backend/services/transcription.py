from pydub import AudioSegment
import speech_recognition as sr

class TranscriptionService:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def transcribe_audio(self, audio_file_path):
        audio = AudioSegment.from_file(audio_file_path)
        audio.export("temp.wav", format="wav")

        with sr.AudioFile("temp.wav") as source:
            audio_data = self.recognizer.record(source)
            try:
                text = self.recognizer.recognize_google(audio_data, language='es-ES')
                return text
            except sr.UnknownValueError:
                return "Error: No se pudo entender el audio."
            except sr.RequestError as e:
                return f"Error: No se pudo solicitar resultados; {e}"