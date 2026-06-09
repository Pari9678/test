class RomanNumeral:
    def __init__(self, number):
        self.number = number

    def convert(self):
        values = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]

        roman = ""
        num = self.number

        for value, symbol in values:
            while num >= value:
                roman += symbol
                num -= value

        return roman


# User input
n = int(input("Enter an integer: "))

# Create object
obj = RomanNumeral(n)

# Display Roman numeral
print("Roman Numeral:", obj.convert())