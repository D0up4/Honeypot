import socket
import json
from datetime import datetime
import os

HOST = '0.0.0.0' #change to your ip
PORT = 22 #use other ports if 22 already in use
LOG_FILE = 'logs/attacks.json'

os.makedirs('logs', exist_ok=True)
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, 'w') as f:
        json.dump([], f)

def log_attack(ip, data):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "ip": ip,
        "data": data
    }
    with open(LOG_FILE, 'r+') as f:
        logs = json.load(f)
        logs.append(entry)
        f.seek(0)
        json.dump(logs, f, indent=4)

def recv_line(conn):
    buffer = b''
    while True:
        data = conn.recv(1)
        if not data or data == b'\n':
            break
        if data != b'\r':
            buffer += data
    return buffer.decode(errors='ignore')

# fake files
fake_files = {
    "passwords.txt": "admin: P@ssw0rd123\nuser: letmein\nroot: toor\n",
    "secret_notes.txt": "The launch is scheduled for next Friday.\nBeware of spies.\n",
    "readme.md": "Welcome to the super secret server. Handle with care.\n"
}

def handle_shell(conn, ip):
    conn.sendall(b"Welcome to Ubuntu 20.04 LTS\n")
    conn.sendall(b"$ ")

    while True:
        cmd = recv_line(conn).strip()
        if not cmd:
            break
        log_attack(ip, f"Command: {cmd}")

        if cmd == "ls":
            files = "  ".join(fake_files.keys()) + "\n"
            conn.sendall(files.encode())
        elif cmd.startswith("cat "):
            filename = cmd[4:].strip()
            content = fake_files.get(filename, f"cat: {filename}: No such file or directory\n")
            conn.sendall(content.encode())
        elif cmd == "whoami":
            conn.sendall(b"root\n")
        elif cmd == "exit":
            conn.sendall(b"Bye!\n")
            break
        else:
            conn.sendall(f"bash: {cmd}: command not found\n".encode())
        conn.sendall(b"$ ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"[+] SSH Honeypot listening on port {PORT}")

    while True:
        conn, addr = s.accept()
        print(f"[!] Connection from {addr[0]}:{addr[1]}")
        conn.sendall(b"SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.3\r\n")

        try:
            max_attempts = 3
            authenticated = False

            for attempt in range(max_attempts):
                conn.sendall(b"login: ")
                username = recv_line(conn).strip()
                if not username:
                    break

                conn.sendall(b"password: ")
                password = recv_line(conn).strip()
                if not password:
                    break

                log_data = f"Attempt {attempt + 1}: Username='{username}', Password='{password}'"
                print(f"[>] {addr[0]} {log_data}")
                log_attack(addr[0], log_data)

                # fake authentication, accept ANY credentials but don't actually grant access
                if attempt == max_attempts - 1:
                    conn.sendall(b"Access granted\r\n")
                else:
                    conn.sendall(b"Access denied\r\n")

            # after max attempts shows a fake shell anyway to keep attacker engaged
            handle_shell(conn, addr[0])

        except Exception as e:
            print(f"[!] Error: {e}")
        finally:
            conn.close()
