from backend.services.transcription import transcribe_audio

def test_transcribe_audio():
    # Test case for a valid audio file
    audio_file_path = "path/to/test_audio.wav"
    expected_transcription = "Expected transcription text from the audio."
    
    transcription_result = transcribe_audio(audio_file_path)
    
    assert transcription_result == expected_transcription, f"Expected: {expected_transcription}, but got: {transcription_result}"

def test_transcribe_audio_invalid_file():
    # Test case for an invalid audio file
    audio_file_path = "path/to/invalid_audio.txt"
    
    try:
        transcription_result = transcribe_audio(audio_file_path)
        assert False, "Expected an exception for invalid audio file"
    except Exception as e:
        assert str(e) == "Invalid audio file format", f"Unexpected exception message: {str(e)}"

def test_transcribe_audio_empty_file():
    # Test case for an empty audio file
    audio_file_path = "path/to/empty_audio.wav"
    
    transcription_result = transcribe_audio(audio_file_path)
    
    assert transcription_result == "", "Expected empty transcription for empty audio file"