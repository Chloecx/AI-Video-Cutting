import requests
import os

API_KEY = "wT3VlSIIPpVQ5PnnThxYc71BJmUETJe5mzo7gm0FVeqHzwOzd4PonJUe"

query = "city night"

url = f"https://api.pexels.com/videos/search?query={query}&per_page=1"

headers = {
    "Authorization": API_KEY
}

response = requests.get(url, headers=headers)

data = response.json()
print(data)

video_url = data["videos"][0]["video_files"][0]["link"]

video_data = requests.get(video_url).content

os.makedirs("downloads", exist_ok=True)

filename = query.replace(" ", "_")

with open(f"downloads/{filename}.mp4", "wb") as f:
    f.write(video_data)

print("视频下载完成")
