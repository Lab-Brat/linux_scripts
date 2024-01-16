from sys import exit
from typing import Dict


class ConversionNum:
    def __init__(self, input_number) -> None:
        self.input_number = self.check_type(input_number)

        # convert to decimal first
        if self.input_number["in_type"] != "dec":
            pass


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

    def to_binary(self):
        number = int(self.input_number["in_num"])
        binary = []

        while number != 0:
            binary.append(number % 2)
            number = number // 2

        return f"bin_{''.join([str(io) for io in binary])}"


    def to_octal(self):
        pass

    def to_decimal(self):
        pass

    def to_hexadecimal(self):
        pass


if __name__ == "__main__":
    input_number = "dec_21"
    con = ConversionNum(input_number)
    print(con.to_binary())
