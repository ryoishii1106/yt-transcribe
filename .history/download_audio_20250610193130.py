import yt_dlp
import tempfile
import os
import uuid


def download_audio_to_tempfile(youtube_url):
    # まず動画情報だけ取得（タイトルを使うため）
    ydl_info_opts = {'quiet': True, 'skip_download': True}
    with yt_dlp.YoutubeDL(ydl_info_opts) as ydl:
        info_dict = ydl.extract_info(youtube_url, download=False)
        video_title = info_dict.get("title", f"audio-{uuid.uuid4()}")

    # ファイル名を安全に（記号除去）
    safe_title = "".join(c for c in video_title if c.isalnum() or c in " _-").strip()
    output_path = f"/tmp/{safe_title}.mp3"

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

    return output_path, safe_title  # ← タイトルも返す！