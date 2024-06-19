def int_to_roman(num):
    Milhar = ["", "M", "MM", "MMM"]
    Centena = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    Dezena = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    Unidade = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    romano_id = Milhar[num // 1000] + Centena[(num % 1000) // 100] + \
                Dezena[(num % 100) // 10] + Unidade[num % 10]

    return romano_id

def roman_to_int(roman):
    nums = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

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

print(int_to_roman(3923))
print(roman_to_int('V'))

