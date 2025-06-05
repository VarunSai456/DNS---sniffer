# DNSpoof-LocalNet

A Python script for performing DNS spoofing and monitoring DNS queries on a local network. This tool utilizes ARP spoofing to intercept traffic and then sniffs DNS requests made by a target device, displaying them in real-time.

---

## ⚠️ Disclaimer

This tool is intended for **educational purposes and ethical security testing only**. Performing DNS spoofing on a network without explicit permission from the network owner is illegal and unethical. The author is not responsible for any misuse or damage caused by this software.

---

## Features

* **ARP Spoofing (MITM):** Puts your machine in the middle of the communication between a target device and the router.
* **DNS Query Monitoring:** Captures and displays DNS queries made by the target device.
* **Real-time Output:** Shows DNS requests with timestamps and clear source/destination information.
* **Colorized Output:** Uses `colorama` for better readability in the terminal.

---

## How it Works

The script operates in two main threads:

1.  **ARP MITM Thread (`mitm` function):** Continuously performs ARP spoofing between the specified `routerip` and `targetip`. This ensures that all traffic, including DNS queries, from the target device passes through your machine.
2.  **DNS Capture Thread (`capture` function):** Sniffs network traffic on the specified interface, specifically looking for UDP packets on port 53 (DNS) originating from the `targetip`. When a DNS query is detected, it extracts the requested domain name and prints it to the console.

---

## Prerequisites

Before running the script, ensure you have the following installed:

* **Python 3**
* **`scapy`**: A powerful interactive packet manipulation program.
* **`colorama`**: For cross-platform colored terminal output.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourUsername/DNSpoof-LocalNet.git](https://github.com/YourUsername/DNSpoof-LocalNet.git)
    cd DNSpoof-LocalNet
    ```
    (Remember to replace `YourUsername` with your actual GitHub username)

2.  **Install dependencies using `pip`:**
    ```bash
    pip install -r requirements.txt
    ```

### Important Notes:

* **Root Privileges:** This script requires root (or administrator) privileges to perform ARP spoofing and packet sniffing. Run it using `sudo` on Linux/macOS.
* **Network Setup:** Ensure your machine is on the same local network as the target device and the router.
* **ARP Cache Poisoning:** This method relies on poisoning the ARP caches of the target and the router. Be aware that this can cause network instability if not managed carefully.

---

## Usage

Run the script from your terminal with the required arguments:

```bash
sudo python3 dns_spoof.py --targetip <TARGET_DEVICE_IP> --iface <YOUR_INTERFACE> --routerip <ROUTER_IP>
