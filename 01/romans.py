def int_to_roman(num):
    Num = int(input("Insira seu número: "))
    Num2 = Num // 1000
    Num3 = (Num % 1000) // 100
    Num4 = (Num % 100) // 10
    Num5 = Num % 10

    Milhar = ["", "m", "mm", "mmm"]
    Centena = ["", "c", "cc", "ccc", "cd", "d", "dc", "dcc", "dccc", "cm"]
    Dezena = ["", "x", "xx", "xxx", "xl", "l", "lx", "lxx", "lxxx", "xc"]
    Unidade = ["", "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix"]

    romano_id = Milhar[Num2] + Centena[Num3] + Dezena[Num4] + Unidade[Num5]

print(romano_id)


def roman_to_int():
    roman = input("Insira seu número em algarismos romanos: ")

    nums = {'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1}

    roman = roman.upper()
    total = 0
    for i in range(len(roman)):
        try:
            value = nums[roman[i]]
            if i + 1 < len(roman) and nums[roman[i + 1]] > value:
                total -= value
            else:
                total += value
        except KeyError:
            raise ValueError('Input is not a valid Roman numeral: %s' % roman)

    return total

print(roman_to_int())
