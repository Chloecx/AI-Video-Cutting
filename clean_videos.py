import os

os.makedirs("clean", exist_ok=True)

videos = sorted(
[
f
for f in os.listdir("downloads")
if f.endswith(".mp4")
]
)

for video in videos:

input_path = os.path.join(
    "downloads",
    video
)

output_path = os.path.join(
    "clean",
    video
)

command = (
    f'ffmpeg -y -i "{input_path}" '
    f'-vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30" '
    f'-c:v libx264 '
    f'-preset fast '
    f'-c:a aac '
    f'"{output_path}"'
)

print(f"处理: {video}")

os.system(command)

print("全部视频清洗完成")
