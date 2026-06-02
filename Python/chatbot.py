from qwen_wrapper import QwenClient
client = QwenClient()
prompt = "What is the current time?"
client.ask(prompt)