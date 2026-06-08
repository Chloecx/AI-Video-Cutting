import requests
import json
import os

PEXELS_API_KEY = "wT3VlSIIPpVQ5PnnThxYc71BJmUETJe5mzo7gm0FVeqHzwOzd4PonJUe"

headers = {
    "Authorization": PEXELS_API_KEY
}

os.makedirs("downloads", exist_ok=True)

with open("storyboard.json", "r", encoding="utf-8") as f:
    storyboard = json.load(f)

for index, shot in enumerate(storyboard, start=1):

    keyword = shot["keyword"]

    print(f"搜索素材: {keyword}")

    url = (
        "https://api.pexels.com/videos/search"
        f"?query={keyword}&per_page=1"
    )

    response = requests.get(
        url,
        headers=headers
    )

    data = response.json()

    if not data.get("videos"):
        print(f"未找到素材: {keyword}")
        continue

    video_url = data["videos"][0]["video_files"][0]["link"]

    video_data = requests.get(video_url).content

    filename = f"downloads/clip{index}.mp4"

    with open(filename, "wb") as f:
        f.write(video_data)

    print(f"已下载: {filename}")

print("全部素材下载完成")
