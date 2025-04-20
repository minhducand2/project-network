from netmiko import ConnectHandler

def evaluate_result(devices):
    result = []
    for dev in devices:
        try:
            conn = ConnectHandler(
                device_type="cisco_ios",
                host=dev["host"],
                username=dev["username"],
                password=dev["password"]
            )
            ospf = conn.send_command("show ip ospf neighbor")
            nat = conn.send_command("show ip nat translations")
            conn.disconnect()
            ospf_status = "✅ OSPF OK" if "Full" in ospf else "❌ OSPF FAIL"
            nat_status = "✅ NAT OK" if ("icmp" in nat or "tcp" in nat) else "❌ NAT FAIL"
            result.append(f"[{dev['host']}] {ospf_status} | {nat_status}")
        except Exception as e:
            result.append(f"[{dev['host']}] ❌ ERROR: {str(e)}")
    return "\n".join(result)
