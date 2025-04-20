from netmiko import ConnectHandler
from agent_local.logger import log_step

def execute_agent_plan(plan_steps, devices):
    logs = []
    for step in plan_steps:
        for device in devices:
            host = device['host']
            creds = {
                "device_type": "cisco_ios",
                "host": host,
                "username": device['username'],
                "password": device['password']
            }
            try:
                log_step(f"\n[{host}] ▶️ {step}", logs)
                with ConnectHandler(**creds) as conn:
                    if 'show' in step or 'ping' in step:
                        out = conn.send_command(step)
                    else:
                        out = conn.send_config_set(step.split('\n'))
                log_step(out, logs)
            except Exception as e:
                log_step(f"[{host}] ❌ ERROR: {str(e)}", logs)
    return logs
