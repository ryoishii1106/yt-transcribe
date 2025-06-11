# yt-transcribe

YouTube音声をWhisperで文字起こしし、Google Docsに自動出力するツール。

## Features
- YouTubeから直接音声抽出（ローカル保存なし）
- Whisperで高精度な文字起こし
- Google Docsに自動アップロード（指定フォルダ）
- 開始時間・時間長の切り出しも可能

## Usage
```bash
python main.py "https://www.youtube.com/watch?v=xxxxxx" --start 00:01:00 --duration 00:00:30
```

## Setup
	•	pip install -r requirements.txt
	•	credentials.json をプロジェクトルートに配置
	•	最初の認証時に token.json が自動生成される
