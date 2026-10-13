import platform
import subprocess


def check_connectivity(target="8.8.8.8"):
    if platform.system() == "Windows":
        command = ["ping", "-n", "4", target]
    else:
        command = ["ping", "-c", "4", target]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=15
        )

        return {
            "target": target,
            "status": "PASS" if result.returncode == 0 else "FAIL",
            "output": result.stdout or result.stderr
        }

    except (subprocess.TimeoutExpired, FileNotFoundError) as error:
        return {
            "target": target,
            "status": "ERROR",
            "output": str(error)
        }