import os

command = """
ffmpeg \
-i clean/sad_woman.mp4 \
-i clean/thinking_person.mp4 \
-i clean/city_night.mp4 \
-filter_complex "[0:v][1:v][2:v]concat=n=3:v=1:a=0[outv]" \
-map "[outv]" \
-c:v libx264 \
final.mp4
"""

os.system(command)

print("视频拼接完成")
