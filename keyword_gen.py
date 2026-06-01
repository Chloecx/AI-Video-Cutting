import requests
import json

script = """
为什么很多人明知道不值得，
却还是舍不得放弃？

这就是沉没成本。

比如一段已经很痛苦的关系，
很多人还是会因为投入太多，
而不愿离开。
"""

prompt = f"""
你是短视频分镜助手。

请根据下面脚本，
为每一句生成适合搜索视频素材的英文关键词。

返回 JSON 格式。

格式示例：
[
  {{
    "text": "原句",
    "keywords": ["keyword1", "keyword2"]
  }}
]

脚本：
{script}
"""

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "qwen2",
        "prompt": prompt,
        "stream": False
    }
)

result = response.json()

print(result["response"])
