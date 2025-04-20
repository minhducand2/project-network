import subprocess
import json
import sys

def run_local_ai_reasoning(prompt):
    try:
        process = subprocess.Popen([
            "ollama", "run", "mistral"
        ], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')

        output, _ = process.communicate(prompt + "\nTrả lời chỉ bằng JSON Python list các bước cần làm.")
        json_str = output.strip().split("```python")[-1].split("```")[-2]
        return json.loads(json_str)
    except Exception as e:
        print("[LLM ERROR]", e)
        return []
