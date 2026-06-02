import ollama
from agent import run_tool
from prompts import SYSTEM_PROMPT

class QwenClient:
    
    def __init__(self, model='qwen2.5-coder:7b', system=SYSTEM_PROMPT):
        self.model = model
        self.system = system

    def ask(self, prompt):
        messages = []
        if self.system:
            messages.append({'role': 'system', 'content': self.system})
        messages.append({'role': 'user', 'content': prompt})
        response = ollama.chat(
            model=self.model,
            messages=messages
        )
        return run_tool(response['message']['content'])