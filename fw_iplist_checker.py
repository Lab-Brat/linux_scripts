import re


class IPChecker:
    def __init__(self, filepath) -> None:
        self.iplist = self.read_file(filepath)

        print("\nAll checks completed :)")

    def read_file(self, filepath):
        with open(filepath, "r") as file:
            ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?:/\d{1,2}|)"
            one_string = "".join(file.readlines())
            return re.findall(ip_pattern, one_string)

if __name__ == "__main__":
    filepath = "./inventory"
    checker = IPChecker(filepath)
