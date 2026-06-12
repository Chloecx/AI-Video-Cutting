import os

videos = sorted(
    [
        f
        for f in os.listdir("clips")
        if f.endswith(".mp4")
    ]
)

if len(videos) == 0:
    print("clips目录为空")
    raise SystemExit

inputs = ""

for video in videos:
    inputs += f'-i "clips/{video}" '

concat_inputs = ""

for i in range(len(videos)):
    concat_inputs += f'[{i}:v]'

filter_complex = (
    f'"{concat_inputs}'
    f'concat=n={len(videos)}:v=1:a=0[outv]"'
)

command = (
    f'ffmpeg -y '
    f'{inputs} '
    f'-filter_complex {filter_complex} '
    f'-map "[outv]" '
    f'-c:v libx264 '
    f'final.mp4'
)

print("开始拼接视频...")

os.system(command)

print("视频拼接完成：final.mp4")
