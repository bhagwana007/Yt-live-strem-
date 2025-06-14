import os
import subprocess
import time

YOUTUBE_STREAM_KEY = os.environ.get("STREAM_KEY")
if not YOUTUBE_STREAM_KEY:
    raise Exception("STREAM_KEY environment variable missing")

INPUT_FILE = os.environ.get("INPUT_FILE", "video.mp4")
LOOP_ARGS = ["-re", "-stream_loop", "-1"] + ["-loop", "1"]

while True:
    cmd = [
        "ffmpeg",
        *LOOP_ARGS,
        "-i", INPUT_FILE,
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-tune", "stillimage",
        "-r", "25",
        "-s", "640x360",
        "-b:v", "900k",
        "-maxrate", "1000k",
        "-bufsize", "1200k",
        "-c:a", "aac",
        "-b:a", "128k",
        "-ar", "44100",
        "-g", "50",
        "-keyint_min", "50",
        "-pix_fmt", "yuv420p",
        "-f", "flv",
        f"rtmp://a.rtmp.youtube.com/live2/{YOUTUBE_STREAM_KEY}"
    ]
    subprocess.run(cmd)
    time.sleep(5)
