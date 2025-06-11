import yt_dlp
import uuid
import subprocess
import os


def download_audio_segment(youtube_url, start_time=None, duration=None):
    temp_id = str(uuid.uuid4())
    full_audio = f"/tmp/{temp_id}_full.m4a"
    clipped_audio = f"/tmp/{temp_id}_clip.mp3"

    # 1. 動画情報を取得（タイトル取得用）
    ydl_info_opts = {'quiet': True, 'skip_download': True}
    with yt_dlp.YoutubeDL(ydl_info_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=False)
        title = info.get("title", f"audio-{temp_id}")

    # 2. 音声をDL
    ydl_opts = {
        'format': 'bestaudio[ext=m4a]',
        'outtmpl': full_audio,
        'quiet': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

    # 3. ffmpegで切り出し（時間指定あり/なし対応）
    cmd = ['ffmpeg', '-i', full_audio]
    if start_time:
        cmd += ['-ss', start_time]
    if duration:
        cmd += ['-t', duration]
    cmd += ['-acodec', 'mp3', '-y', clipped_audio]
    subprocess.run(cmd, check=True)

    os.remove(full_audio)
    return clipped_audio, title