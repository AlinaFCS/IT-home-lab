"""
Readable version of ping_sweep.py.

The actual script in this folder is a one-line version — that's not a style choice,
it's because copying multi-line scripts into this VM through the VirtualBox clipboard
kept losing line breaks, which breaks anything relying on Python's indentation. Chaining
everything with semicolons on one line sidesteps that problem entirely. This version is
here so the logic is actually readable.
"""

import subprocess
import platform

hosts = {
    "DC01": "192.168.10.1",
    "Client01": "192.168.10.2",
}

print("Network Status Check")
print("-" * 30)

for name, ip in hosts.items():
    param = "-n" if platform.system().lower() == "windows" else "-c"
    result = subprocess.run(
        ["ping", param, "1", ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    status = "UP" if result.returncode == 0 else "DOWN"
    print(f"{name} ({ip}): {status}")

print("-" * 30)
print("Check complete.")
