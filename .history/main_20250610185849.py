from download_audio import download_audio_to_tempfile
from transcribe import transcribe_audio
from write_to_gdoc import write_to_google_doc
import sys
import os

def main(youtube_url):
    print("🔽 YouTube音声を一時ファイルとして取得中...")
    audio_path = download_audio_to_tempfile(youtube_url)

    try:
        print("🧠 Whisperで文字起こし中...")
        transcript = transcribe_audio(audio_path)

        print("📄 Google Docs に書き込み中...")
        doc_url = write_to_google_doc(transcript, title="YouTube文字起こし")
        print("✅ 完了！ドキュメントはこちら：")
        print(doc_url)

    finally:
        # 実行後にファイル削除
        if os.path.exists(audio_path):
            os.remove(audio_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使い方: python main.py <YouTubeのURL>")
        sys.exit(1)

    main(sys.argv[1])