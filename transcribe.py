import whisper


def transcribe_audio(file_path):
    model = whisper.load_model("base")  # small, medium, large も可
    result = model.transcribe(file_path)
    return result["text"]