# Bulk Configuration Script Generator

This Python project helps automate the generation of network device configuration scripts based on a simple CSV file input. It's especially useful for quickly setting up Cisco Packet Tracer labs or preparing initial device configurations.

---

## 🔧 Features

- Supports multiple interfaces per device
- Automatically handles VLAN assignment and IP configuration
- Generates a configuration script per device
- Speeds up lab setup for CCNA, Packet Tracer, or learning environments
- Beginner-friendly, no external Python libraries required

---

## 📁 Project Structure

```
bulk_config_script_generator/
├── generate_bulk_configs.py     # Main script
├── devices.csv                  # Input file with device details
├── README.md                    # Documentation (this file)
├── Switch1_config.txt           # Example output
├── Router1_config.txt           # Example output
```

---

## 📥 Input Format (devices.csv)

Each row in the CSV defines an interface on a device.

### Example:

```csv
hostname,interface,ip,subnet,vlan
Switch1,FastEthernet0/1,192.168.10.1,255.255.255.0,10
Switch1,FastEthernet0/2,192.168.20.1,255.255.255.0,20
Router1,GigabitEthernet0/0,10.10.10.1,255.255.255.252,
Router1,GigabitEthernet0/1,192.168.30.1,255.255.255.0,
```

---

## 🚀 How to Use

1. Clone the repo or download the folder
2. Modify the `devices.csv` file with your device/interface data
3. Run the script:

```bash
python generate_bulk_configs.py
```

4. Config files like `Switch1_config.txt`, `Router1_config.txt`, etc. will be generated in the same folder.

---

## 💡 How to Use with Cisco Packet Tracer

Since Packet Tracer does not support direct SSH/API access, here's how to apply the config:

1. Open your lab in Packet Tracer
2. Create the corresponding devices (Switch1, Router1, etc.)
3. Open the **CLI tab** for each device
4. Copy-paste the config from the generated `.txt` file into the CLI

This simulates what automation would do in real network gear.

---

## 📌 Sample Output (`Switch1_config.txt`)

```
enable
configure terminal
hostname Switch1
interface FastEthernet0/1
switchport access vlan 10
ip address 192.168.10.1 255.255.255.0
no shutdown
exit
interface FastEthernet0/2
switchport access vlan 20
ip address 192.168.20.1 255.255.255.0
no shutdown
exit
end
write memory
```

---

## 🧑‍💻 Author

**Susmitha**  
GitHub: [@Susmitha2511](https://github.com/Susmitha2511)

---

## 📜 License

This project is licensed under the MIT License.

---

## 🙌 Contributions

Pull requests and suggestions are welcome! If you found this project helpful, feel free to star ⭐ the repo and share it with others.
