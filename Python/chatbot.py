import sys
print(sys.executable)

import ollama

import requests

r = requests.get("http://localhost:11434/api/tags")
print(r.json())


response = ollama.chat(
    model='qwen2.5-coder:7b',
    messages=[
        {
            'role': 'user',
            'content': 'Explain how AI works in 200 words'
        }
    ]
)

print(response['message']['content'])