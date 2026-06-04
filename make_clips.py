import os

shots = [
    ("sad_woman.mp4", 4),
    ("thinking_person.mp4", 3),
    ("city_night.mp4", 5)
]

os.makedirs("clips", exist_ok=True)

for i, (video, duration) in enumerate(shots, start=1):
    input_file = f"clean/{video}"
    output_file = f"clips/clip{i}.mp4"

    cmd = (
        f'ffmpeg -y -i "{input_file}" '
        f'-t {duration} '
        f'-c copy '
        f'"{output_file}"'
    )

    os.system(cmd)

print("所有镜头裁切完成")
