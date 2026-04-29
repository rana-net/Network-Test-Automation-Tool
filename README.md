# 🚀 Network Test Automation Tool

A Python-based network testing framework that automates system health checks over SSH.

## 🔧 Features

* Remote command execution using SSH (Paramiko)
* Automated network validation:

  * Ping Test
  * Routing Table Check
  * Open Ports Check
  * Traceroute
* JSON-based configuration for scalability
* Modular validation engine

## 🛠 Tech Stack

* Python
* Paramiko (SSH)
* Linux Networking Commands
* JSON Configuration

## 📂 Project Structure

```
main.py                # Main execution script  
device_connection.py  # SSH connection & command execution  
validator.py          # Output validation logic  
logger.py             # Logs test results  
tests.json            # Test configuration  
```

## ▶️ How to Run

1. Install dependencies:

```
pip install paramiko
```

2. Run the script:

```
python main.py
```

## 📊 Sample Output

```
[TEST] Ping Google
✅ PASS

[TEST] Check Routing Table
✅ PASS

[TEST] Check Open Ports
✅ PASS

[TEST] Traceroute Test
✅ PASS
```

## 🧠 What I Learned

* SSH automation and remote system management
* Linux networking commands and diagnostics
* Debugging real-world connection issues
* Writing scalable and modular Python code

## 🚀 Future Improvements

* Multi-device parallel execution
* Web dashboard for visualization
* Alerting system (email/Slack)
* Integration with Prometheus/Grafana

