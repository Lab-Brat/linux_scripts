from sys import exit
from typing import Dict


class ConversionNum:
    def __init__(self, input_number) -> None:
        self.input_number = self.check_type(input_number)

    def check_type(self, input_number: str) -> Dict:
        input_type, input_number = input_number.split("_")
        
        match input_type:
            case "bin" | "oct" | "dec" | "hex":
                return {
                    "in_type": input_type,
                    "in_num": input_number,
                }
            case _:
                print(f"wrong type prefix: {input_number}")
                print("type should be one of these: bin oct dec hex")
                exit(1)

    def _make_decimal(self):
        number = self.input_number["in_num"]
        nutype = self.input_number["in_type"]
        result = self.to_decimal(number, nutype)
        if result is not None:
            return int(result.split("_")[1])

    def to_binary(self):
        if self.input_number["in_type"] != "dec":
            number = self._make_decimal()
        else:
            number = int(self.input_number["in_num"])
        print(number)
        binary = []

        while number != 0:
            binary.append(number % 2)
            number = number // 2

        return f"bin_{''.join([str(io) for io in binary[::-1]])}"


    def to_octal(self):
        pass

    def _to_decimal(self, number, base):
        power = len(number) - 1
        result = 0
        hex_dict = {
            "A": "10",
            "B": "11",
            "C": "12",
            "D": "13",
            "E": "14",
            "F": "15",
        }

        for digit in list(number):
            if digit in ["A", "B", "C", "D", "E", "F"]:
                digit = hex_dict[digit]
            result += int(digit) * (base ** power)
            power -= 1

        return f"dec_{result}"

    def to_decimal(self, number=None, nutype=None):
        if number == None and nutype ==None:
            number = self.input_number["in_num"]
            nutype = self.input_number["in_type"]

        match nutype:
            case "bin":
                return self._to_decimal(number, 2)
            case "oct":
                return self._to_decimal(number, 8)
            case "dec":
                return number
            case "hex":
                return self._to_decimal(number, 16)

    def to_hexadecimal(self):
        pass


if __name__ == "__main__":
    input_number = "dec_10"
    input_number = "oct_16"
    con = ConversionNum(input_number)
    print(con.to_binary())
