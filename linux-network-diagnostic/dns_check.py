import socket


def check_dns(domain="example.com"):
    try:
        addresses = socket.getaddrinfo(
            domain, None, family=socket.AF_INET
        )
        ips = sorted({item[4][0] for item in addresses})

        return {
            "domain": domain,
            "status": "PASS",
            "ip_addresses": ips
        }

    except socket.gaierror as error:
        return {
            "domain": domain,
            "status": "FAIL",
            "ip_addresses": [],
            "error": str(error)
        }