from services.audio_ingest import AudioIngest
from services.audio_preprocessing import AudioPreprocessing
from services.transcription import Transcription
from services.embedding_model import EmbeddingModel
from services.nlp_pipeline import NLPipeline
from services.report_builder import ReportBuilder
from models.report import Report

class Inference:
    def __init__(self):
        self.audio_ingest = AudioIngest()
        self.audio_preprocessing = AudioPreprocessing()
        self.transcription = Transcription()
        self.embedding_model = EmbeddingModel()
        self.nlp_pipeline = NLPipeline()
        self.report_builder = ReportBuilder()

    def process_audio(self, audio_file):
        audio_data = self.audio_ingest.ingest(audio_file)
        preprocessed_audio = self.audio_preprocessing.preprocess(audio_data)
        transcribed_text = self.transcription.transcribe(preprocessed_audio)
        embeddings = self.embedding_model.generate_embeddings(transcribed_text)
        report_data = self.nlp_pipeline.generate_report(embeddings)
        report = self.report_builder.build_report(report_data)

        return report

    def save_report(self, report):
        report.save()  # Assuming the Report model has a save method to persist the report.