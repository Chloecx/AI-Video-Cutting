import subprocess

input_file = "input.mp4"

clips = [
    (0, 5),
    (10, 15),
    (20, 25)
]

output_files = []

for i, (start, end) in enumerate(clips):
    out = f"clip_{i}.mp4"

    cmd = [
        "ffmpeg",
        "-y",
        "-i", input_file,
        "-ss", str(start),
        "-to", str(end),
        "-c", "copy",
        out
    ]

    subprocess.run(cmd)
    output_files.append(out)

with open("list.txt", "w") as f:
    for file in output_files:
        f.write(f"file '{file}'\n")

subprocess.run([
    "ffmpeg",
    "-y",
    "-f", "concat",
    "-safe", "0",
    "-i", "list.txt",
    "-c", "copy",
    "output.mp4"
])

print("完成！输出文件：output.mp4")
