import requests
import json
import re

# 读取脚本文件
with open("script.txt", "r", encoding="utf-8") as f:
    script = f.read()

prompt = f"""
你是一名短视频分镜师。

请根据下面脚本生成分镜。

要求：

1. 只输出JSON数组
2. 不要输出任何解释
3. 不要输出Markdown代码块
4. 每个镜头包含：
   - keyword
   - duration
5. keyword必须是适合Pexels搜索的视频关键词
6. duration控制在3到5秒之间

示例：

[
  {{
    "keyword": "sad woman",
    "duration": 4
  }},
  {{
    "keyword": "thinking person",
    "duration": 3
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

result = response.json()["response"]

# 提取 JSON 数组
match = re.search(r"\[.*\]", result, re.DOTALL)

if match is None:
    print("错误：未找到有效JSON")
    print(result)
    raise SystemExit

json_text = match.group(0)

try:
    storyboard = json.loads(json_text)

    with open(
        "storyboard.json",
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            storyboard,
            f,
            ensure_ascii=False,
            indent=4
        )

    print("分镜保存成功：storyboard.json")

except json.JSONDecodeError:
    print("错误：JSON解析失败")
    print(json_text)
