import re
import ipaddress


class IPChecker:
    def __init__(self, filepath) -> None:
        iplist = self.read_file(filepath)
        ips, networks, invalid = self.categorize_addresses(iplist)
        print(len(ips), len(networks), len(invalid))

        print("\nAll checks completed :)")

    def read_file(self, filepath):
        with open(filepath, "r") as file:
            ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?:/\d{1,2}|)"
            one_string = "".join(file.readlines())
            return re.findall(ip_pattern, one_string)

    def categorize_addresses(self, iplist):
        ips = []
        networks = []
        invalid = []
        for address in iplist:
            try:
                if "/" in address:
                    networks.append(ipaddress.IPv4Network(address))
                else:
                    ips.append(ipaddress.IPv4Address(address))
            except:
                invalid.append(address)

        if invalid:
            print(f"invalid addresses found:")
            for address in invalid:
                print(address)

        return ips, networks, invalid


if __name__ == "__main__":
    filepath = "./inventory"
    checker = IPChecker(filepath)
