from download_audio import download_audio
from transcribe import transcribe_audio
from write_to_gdoc import write_to_google_doc

if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=..."  # 任意の動画URL
    audio_file = "audio.mp3"

    print("🔽 ダウンロード中...")
    download_audio(url, audio_file)

    print("🎙 音声を文字起こし中...")
    transcript = transcribe_audio(audio_file)

    print("📄 Google Docs に書き込み中...")
    write_to_google_doc(transcript, title="YouTube文字起こし")

    print("✅ 完了！")