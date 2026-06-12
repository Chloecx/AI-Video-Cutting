import os
import json

os.makedirs("clips", exist_ok=True)

with open(
    "storyboard.json",
    "r",
    encoding="utf-8"
) as f:
    storyboard = json.load(f)

videos = sorted(
    [
        f
        for f in os.listdir("clean")
        if f.endswith(".mp4")
    ]
)

for index, shot in enumerate(storyboard):

    if index >= len(videos):
        break

    duration = shot["duration"]

    input_file = os.path.join(
        "clean",
        videos[index]
    )

    output_file = os.path.join(
        "clips",
        f"clip{index+1}.mp4"
    )

    command = (
        f'ffmpeg -y '
        f'-i "{input_file}" '
        f'-t {duration} '
        f'-c copy '
        f'"{output_file}"'
    )

    print(
        f"裁切 {videos[index]} -> {duration}秒"
    )

    os.system(command)

print("全部镜头生成完成")
