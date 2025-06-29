# 🎙️ yt-transcribe

**yt-transcribe** is a Python-based tool that automatically transcribes audio from YouTube videos using OpenAI's Whisper and uploads the result to Google Docs.

---

## 🌽 Features

- 🔗 Download audio from YouTube (without saving full video files)  
- 🧠 Transcribe with Whisper (supports time range selection)  
- 📄 Auto-create Google Docs in a target Drive folder  
- ⚙️ Optional CLI arguments: start time & duration  
- 🧹 No large audio files remain after execution  

---

## 📋 Requirements

- Python 3.11+  
- [ffmpeg](https://ffmpeg.org/)  
- [OpenAI Whisper](https://github.com/openai/whisper)  
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)  
- Google Cloud credentials (Docs API & Drive API enabled)  

---

## 🔧 Setup

1. **Clone the repository and create a virtual environment:**

    ```bash
    git clone https://github.com/ryoishii1106/yt-transcribe.git
    cd yt-transcribe
    python3 -m venv yt-transcribe-env
    source yt-transcribe-env/bin/activate # Testing whether it can be activated
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up Google Cloud credentials:**

    - Place your `credentials.json` in the root directory.
    - The script will generate `token.json` upon first authentication.

---

## 🎬 Usage
### 🔹 Activation of a virtual environment
```bash
source yt-transcribe-env/bin/activate
```
### 🔹 Basic usage
```bash
python main.py "https://www.youtube.com/watch?v=XXXXXXXX"
```
### 🔹 With time range (optional)
```bash
python main.py "https://www.youtube.com/watch?v=XXXXXXXX" --start 00:01:30 --duration 00:00:45
```

---

## 🚀 Output
	•	Transcription is saved to a new Google Doc with the YouTube video title.
	•	The document is placed in your Drive’s ShadowingScript folder.
	•	Folder will be auto-created if it doesn’t exist.

---

## 🗂 Project Structure
```
yt-transcribe/
├── main.py
├── transcribe.py
├── download_audio_segment.py
├── write_to_gdoc.py
├── google_auth_setup.py
├── requirements.txt
├── .gitignore
├── README.md
└── (excluded) credentials.json, token.json
```

---

## 📝 Notes
These files should be excluded (already in .gitignore):
	•	credentials.json
	•	token.json
	•	.env (if applicable)

---

## 📄 License
MIT License

---

## 👶 Author
Created by @ryoishii1106

Pull requests and suggestions welcome!






