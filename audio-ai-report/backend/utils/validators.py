from flask import request, jsonify

def validate_audio_file(file):
    if not file:
        return False, "No file provided"
    if not file.filename.endswith(('.wav', '.mp3', '.m4a')):
        return False, "Invalid file format. Supported formats: .wav, .mp3, .m4a"
    return True, ""

def validate_report_data(data):
    if 'title' not in data or not data['title']:
        return False, "Title is required"
    if 'content' not in data or not data['content']:
        return False, "Content is required"
    return True, ""