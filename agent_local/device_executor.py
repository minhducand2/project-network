from netmiko import ConnectHandler

def execute_plan_on_devices(plan, devices):
    logs = []
    for step in plan:
        for dev in devices:
            try:
                conn = ConnectHandler(
                    device_type="cisco_ios",
                    host=dev["host"],
                    username=dev["username"],
                    password=dev["password"]
                )
                if "ospf" in step.lower():
                    cmds = [
                        "router ospf 1",
                        "network 192.168.1.0 0.0.0.255 area 0",
                        "network 10.10.10.0 0.0.0.255 area 0"
                    ]
                    res = conn.send_config_set(cmds)
                elif "nat" in step.lower():
                    cmds = [
                        "interface g0/1", "ip nat outside",
                        "interface g0/0", "ip nat inside",
                        "ip nat inside source list 1 interface g0/1 overload",
                        "access-list 1 permit 192.168.0.0 0.0.0.255"
                    ]
                    res = conn.send_config_set(cmds)
                elif "neighbor" in step.lower():
                    res = conn.send_command("show ip ospf neighbor")
                    if "Full" not in res:
                        res += "\n⚠️ Neighbor không lên!"
                elif "ping" in step.lower():
                    res = conn.send_command("ping 10.10.10.2")
                else:
                    res = conn.send_command(step)
                conn.disconnect()
                logs.append(f"[{dev['host']}] {step}\n{res}\n")
            except Exception as e:
                logs.append(f"[{dev['host']}] ERROR: {str(e)}")
    return "\n".join(logs)
