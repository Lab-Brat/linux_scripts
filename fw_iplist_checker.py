import re
import ipaddress
from collections import Counter


class IPChecker:
    def __init__(self, filepath) -> None:
        iplist = self.read_file(filepath)
        ips, networks, _ = self.categorize_addresses(iplist)
        if ips:
            print(f"found IP addresses: {len(ips)}")
        if networks:
            print(f"found Networks: {len(networks)}")
        if ips == [] and networks == []:
            print("Did not find any valid IPs or networks, exiting")
            exit()
        else:
            print()

        # find duplicates
        self.find_duplicates(networks)
        self.find_duplicates(ips)

        # find overlap in network ranges
        self.find_subnet_overlaps(networks)

        # find network and IP overlaps
        self.find_overlaps(networks, ips)

        print("All checks completed :)")

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
            print()

        return ips, networks, invalid

    def find_duplicates(self, ipset):
        counter = Counter(ipset)
        duplicates = [
            item for item, frequency in counter.items() if frequency > 1
        ]
        if duplicates:
            print("duplicates found!")
            for dup in duplicates:
                print(dup)
            print()

    def find_subnet_overlaps(self, subnets):
        # get only the unique set of subnets
        subnets = list(set(subnets))
        # Convert subnets into ranges of IPs
        ip_ranges = [ipaddress.IPv4Network(subnet) for subnet in subnets]

        extra_space = False
        for i in range(len(ip_ranges)):
            for j in range(i + 1, len(ip_ranges)):
                if ip_ranges[i].overlaps(ip_ranges[j]):
                    print(f"Subnets {subnets[i]} and {subnets[j]} overlap.")
                    extra_space = True
        if extra_space:
            print()

    def find_overlaps(self, nets, ips):
        extra_space = False
        for net in nets:
            net = ipaddress.ip_network(net)
            for ip in ips:
                ip = ipaddress.ip_address(ip)
                if ip in net:
                    print(f"Overlap Found: {net} covers {ip}")
                    extra_space = True
        if extra_space:
            print()


if __name__ == "__main__":
    filepath = "./inventory"
    checker = IPChecker(filepath)
