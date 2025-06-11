import yt_dlp
import tempfile
import os

def download_audio_to_tempfile(youtube_url):
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_audio:
        output_path = temp_audio.name

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

    return output_path