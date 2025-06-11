import yt_dlp
import tempfile
import os
import uuid


def download_audio_to_tempfile(youtube_url):
    # 一時的な .mp3 ファイル名を UUIDで生成（OS上のファイル名として問題ない）
    output_path = f"/tmp/{uuid.uuid4()}.mp3"

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path.replace('.mp3', '.%(ext)s'),
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