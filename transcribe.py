from faster_whisper import WhisperModel

model = WhisperModel("base")

segments, info = model.transcribe("input.mp4")

with open("output.srt", "w", encoding="utf-8") as f:
    count = 1

    for segment in segments:
        start = segment.start
        end = segment.end
        text = segment.text

        def format_time(seconds):
            hrs = int(seconds // 3600)
            mins = int((seconds % 3600) // 60)
            secs = int(seconds % 60)
            millis = int((seconds - int(seconds)) * 1000)

            return f"{hrs:02}:{mins:02}:{secs:02},{millis:03}"

        f.write(f"{count}\n")
        f.write(f"{format_time(start)} --> {format_time(end)}\n")
        f.write(f"{text.strip()}\n\n")

        count += 1

print("字幕生成完成：output.srt")
