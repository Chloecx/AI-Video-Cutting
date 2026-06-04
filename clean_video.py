import os

videos = [
    "sad_woman.mp4",
    "thinking_person.mp4",
    "city_night.mp4"
]

for video in videos:
    input_path = f"downloads/{video}"
    output_path = f"clean/{video}"

    command = (
        f'ffmpeg -y -i "{input_path}" '
        f'-vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30" '
        f'-c:v libx264 -preset fast '
        f'-c:a aac '
        f'"{output_path}"'
    )

    os.system(command)

print("全部视频清洗完成")
