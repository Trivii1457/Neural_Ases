from flask import Flask, jsonify, request
from backend.services.audio_ingest import AudioIngest
from backend.services.transcription import Transcription
from backend.services.nlp_pipeline import NLPipeline
from backend.services.pdf_generator import PDFGenerator
from backend.models.report import Report
from backend.database.session import db_session

def test_generate_report(client):
    audio_file = open('tests/test_audio.wav', 'rb')
    response = client.post('/api/reports', data={'audio': audio_file})
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'pdf_url' in json_data
    assert 'dimensions' in json_data
    assert 'generated_text' in json_data

def test_report_not_found(client):
    response = client.get('/api/reports/invalid_report_id')
    assert response.status_code == 404
    json_data = response.get_json()
    assert json_data['error'] == 'Report not found'

def test_audio_ingest(client):
    audio_file = open('tests/test_audio.wav', 'rb')
    response = client.post('/api/audio/ingest', data={'audio': audio_file})
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['message'] == 'Audio ingested successfully'