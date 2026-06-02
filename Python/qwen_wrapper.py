import ollama

class QwenClient:
    
    def __init__(self, model='qwen2.5-coder:7b'):
        self.model = model

    def ask_qwen(self, prompt):
        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    'role': 'user',
                    'content': prompt
                }
            ]
        )
        return response['message']['content']   