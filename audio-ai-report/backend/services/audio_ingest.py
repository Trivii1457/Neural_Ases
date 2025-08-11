from flask import Flask, request, jsonify
import os
import uuid
from backend.utils.file_storage import save_audio_file

def ingest_audio():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400

    audio_file = request.files['audio']
    if audio_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Generate a unique filename
    unique_filename = f"{uuid.uuid4()}.wav"
    audio_path = os.path.join("/tmp", unique_filename)

    # Save the audio file
    save_audio_file(audio_file, audio_path)

    return jsonify({'message': 'Audio file ingested successfully', 'audio_path': audio_path}), 200