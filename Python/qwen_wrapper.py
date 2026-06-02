import ollama
from agent import run_tool
from prompts import SYSTEM_PROMPT
from database import save_message, load_messages, get_latest_system

class QwenClient:
    
    def __init__(self, model='qwen2.5-coder:7b', system=SYSTEM_PROMPT):
        self.model = model
        self.system = system

    def ask(self, prompt):
        messages = []
        if self.system:
            latest_system = get_latest_system()
            if latest_system != self.system:
                save_message('system', self.system)
            messages.append({'role': 'system', 'content': self.system})
        messages.append({'role': 'user', 'content': prompt})
        save_message('user', prompt)
        response = ollama.chat(
            model=self.model,
            messages=messages
        )
        save_message('assistant', response['message']['content'])
        return run_tool(response['message']['content'])