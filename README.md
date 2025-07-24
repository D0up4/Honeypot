# 🐝 Honeypot Cybersecurity Portfolio

Welcome to my Honeypot project portfolio. This repository demonstrates the design, deployment, and analysis of a cybersecurity honeypot used to **detect**, **log**, and **study malicious activities** in a controlled environment.

---
Author: D0up4
Project Type: Blue Team Recon
Last Updated: 07/2025
---
## 📌 Project Overview

A **honeypot** is a decoy system or service set up to attract cyber attackers. This project simulates vulnerable systems in order to:

- 🛡 Detect and analyze intrusion attempts  
- 🧠 Study attacker behavior and tactics  
- 🔎 Enhance threat intelligence  
- 🧰 Improve defensive strategies  

This portfolio includes configuration files, deployment scripts, and analysis reports based on real-world attack data.

---

## 🧰 Tools & Technologies

| Category     | Tools / Technologies Used |
|--------------|---------------------------|
| Honeypots    |  Custom SSH/Telnet Traps  |
| Environment  |  Ubuntu Server            |
| Logging      |  Text-Based Logs          |
| Scripting    |  Python, Bash             |

---

## 🧪 Deployment Guide Clone the repo

git clone https://github.com/D0up4/Honeypot cd honeypot-portfolio 
Set up the environment Follow the setup guide:

Run the honeypot Depending on the tool (e.g., Docker + Cowrie)

In Command Prompt:

python ssh_honeypot.py And you should see: [+] SSH Honeypot listening on port 22

On attacker side, In Command Prompt: telnet 0.0.0.0 (replace with actual host ip) 22 (or any other port its hosted on)

---

🔐 Legal & Ethical Notice Disclaimer: This project is for educational and research purposes only. All deployments were done in isolated, controlled environments with no risk to production systems. Do not expose honeypots to public networks without understanding the security implications.
