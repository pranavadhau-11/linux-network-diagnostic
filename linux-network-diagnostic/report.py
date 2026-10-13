from datetime import datetime


def save_report(content):
    filename = "network_report.txt"

    with open(filename, "a", encoding="utf-8") as file:
        file.write("\n" + "=" * 40 + "\n")
        file.write(f"Date: {datetime.now()}\n")
        file.write(content + "\n")

    return filename