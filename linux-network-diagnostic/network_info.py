import platform
import socket
import subprocess


def get_hostname():
    return socket.gethostname()


def get_os():
    return platform.system()


def get_ip_info():
    system = platform.system()

    if system == "Windows":
        command = ["ipconfig"]
    else:
        command = ["ip", "addr"]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.stdout or result.stderr

    except (subprocess.TimeoutExpired, FileNotFoundError) as error:
        return f"Error: {error}"