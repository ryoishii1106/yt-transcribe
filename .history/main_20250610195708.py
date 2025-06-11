import argparse
import os
from download_audio_segment import download_audio_segment
from transcribe import transcribe_audio
from write_to_gdoc import write_to_google_doc

def main():
    parser = argparse.ArgumentParser(description="YouTube動画の文字起こしをGoogle Docsに出力")
    parser.add_argument("url", help="YouTube動画のURL")
    parser.add_argument("--start", help="切り出し開始時間 (例: 00:01:30)", default=None)
    parser.add_argument("--duration", help="切り出し時間長 (例: 00:01:00)", default=None)

    args = parser.parse_args()
    youtube_url = args.url
    start_time = args.start
    duration = args.duration

    folder_id = "YOUR_SHADOWING_SCRIPT_FOLDER_ID"  # ← 固定でOK

    print("🔽 YouTube音声を一時ファイルとして取得中...")
    audio_path, video_title = download_audio_segment(
        youtube_url, start_time=start_time, duration=duration
    )

    try:
        print("🧠 Whisperで文字起こし中...")
        transcript = transcribe_audio(audio_path)

        print("📄 Google Docs に書き込み中...")
        doc_url = write_to_google_doc(transcript, title=video_title, folder_id=folder_id)
        print("✅ 完了！ドキュメントはこちら：")
        print(doc_url)

    finally:
        if os.path.exists(audio_path):
            os.remove(audio_path)

if __name__ == "__main__":
    main()