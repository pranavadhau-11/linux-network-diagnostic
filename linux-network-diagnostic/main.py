from network_info import get_hostname, get_os, get_ip_info
from connectivity import check_connectivity
from dns_check import check_dns
from report import save_report


def main():
    print("=" * 45)
    print(" LINUX NETWORK DIAGNOSTIC TOOL")
    print("=" * 45)

    report = []

    hostname = get_hostname()
    os_name = get_os()

    print(f"\nHostname: {hostname}")
    print(f"Operating System: {os_name}")

    report.append(f"Hostname: {hostname}")
    report.append(f"Operating System: {os_name}")

    print("\n--- Network Information ---")
    ip_info = get_ip_info()
    print(ip_info)
    report.append("--- Network Information ---\n" + ip_info)

    print("\n--- Connectivity Check ---")
    connectivity = check_connectivity()
    print("Target:", connectivity["target"])
    print("Status:", connectivity["status"])
    report.append(
        f"Connectivity: {connectivity['target']} - "
        f"{connectivity['status']}"
    )

    print("\n--- DNS Check ---")
    dns = check_dns()
    print("Domain:", dns["domain"])
    print("Status:", dns["status"])

    if dns["ip_addresses"]:
        print("IP addresses:", ", ".join(dns["ip_addresses"]))

    report.append(f"DNS: {dns['domain']} - {dns['status']}")

    filename = save_report("\n".join(report))
    print(f"\nReport saved to: {filename}")


if __name__ == "__main__":
    main()