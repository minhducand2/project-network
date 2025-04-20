def log_step(text, logs):
    print(text)
    logs.append(text)

def print_result(logs):
    print("\n📝 Đánh giá:")
    for entry in logs:
        print(entry)

def save_log_file(logs):
    from datetime import datetime
    import os
    os.makedirs("logs", exist_ok=True)
    with open(f"logs/log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt", "w", encoding='utf-8') as f:
        f.write('\n'.join(logs))
