import pandas as pd
from collections import defaultdict

def generate_bulk_configs(csv_file):
    df = pd.read_csv(csv_file)
    device_configs = defaultdict(list)

    for _, row in df.iterrows():
        interface = row['interface']
        ip = row['ip']
        subnet = row['subnet']
        vlan = row.get('vlan')

        lines = [f"interface {interface}"]
        if pd.notna(vlan):
            lines.append(f"switchport access vlan {int(vlan)}")
        lines.append(f"ip address {ip} {subnet}")
        lines.append("no shutdown")
        lines.append("exit")

        device_configs[row['hostname']].extend(lines)

    for hostname, commands in device_configs.items():
        config_lines = [
            "enable",
            "configure terminal",
            f"hostname {hostname}"
        ] + commands + [
            "end",
            "write memory"
        ]
        with open(f"{hostname}_config.txt", "w") as f:
            f.write("\n".join(config_lines))

if __name__ == "__main__":
    generate_bulk_configs("devices.csv")
