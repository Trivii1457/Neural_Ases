from flask import Blueprint, request, jsonify
from backend.services.audio_ingest import AudioIngest
from backend.services.audio_preprocessing import AudioPreprocessing
from backend.services.transcription import Transcription
from backend.services.nlp_pipeline import NLPipeline
from backend.services.report_builder import ReportBuilder
from backend.services.pdf_generator import PDFGenerator

reports_bp = Blueprint('reports', __name__)

@reports_bp.route('/generate', methods=['POST'])
def generate_report():
    audio_file = request.files.get('audio')
    if not audio_file:
        return jsonify({'error': 'No audio file provided'}), 400

    audio_ingest = AudioIngest()
    audio_path = audio_ingest.save_audio(audio_file)

    audio_preprocessing = AudioPreprocessing()
    preprocessed_audio = audio_preprocessing.process(audio_path)

    transcription_service = Transcription()
    transcribed_text = transcription_service.transcribe(preprocessed_audio)

    nlp_pipeline = NLPipeline()
    report_data = nlp_pipeline.process(transcribed_text)

    report_builder = ReportBuilder()
    report = report_builder.build(report_data)

    pdf_generator = PDFGenerator()
    pdf_path = pdf_generator.generate(report)

    return jsonify({
        'message': 'Report generated successfully',
        'pdf_url': pdf_path
    })