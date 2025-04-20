from agent_local.llm_local import run_local_ai_reasoning
from agent_local.netmiko_executor import execute_agent_plan
from agent_local.logger import print_result, save_log_file  # ✅ Đã bỏ print_log
from config.devices_config import USING_DEVICES

print("🚀 Starting AI Network Engineer Agent (Local via Ollama)...")

while True:
    user_input = input("\n💬 Nhập đề bài cấu hình (hoặc 'exit'): ")
    if user_input.lower() == "exit":
        break

    print("\n🧠 Đề bài:", user_input)
    print("🤖 Đang phân tích với Mistral local...")

    plan = run_local_ai_reasoning(user_input)

    print("\n✍️ Kế hoạch hành động:", plan)
    print("\n📃 Ghi chú log:")

    full_log = execute_agent_plan(plan, USING_DEVICES)

    print_result(full_log)
    save_log_file(full_log)
