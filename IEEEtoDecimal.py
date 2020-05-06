def partition_number(s):
    return s[0], s[1:9], s[9:32]


def convert_bias(s):
    return int(binary_to_decimal(s)) - 127


def binary_to_decimal(s):
    s = s[::-1]
    ans = 0
    display = ""
    for enum, i in enumerate(s):
        if i == "1":
            ans += pow(2, enum)
            display += "2^" + str(enum)
            if enum < len(s) - 1:
                display += " + "
    print(display + " = " + str(ans) + " - 127 = " + str(ans - 127))
    return ans


def below_binary_to_decimal(s):
    ans = 0
    display = ""
    for enum, i in enumerate(s):
        if i == "1":
            ans += pow(2, -(enum + 1))
            display += "2^" + str(-(enum + 1))
            if enum < len(s) - 1:
                display += " + "
    print(display)
    return ans


def ieee_equation(sign, exp, mant):
    start = str(pow(-1, sign) * (1 + mant))
    end = " x 2 ^ " + str(exp)
    return start + end


def convert(s):
    s = s.replace(" ", "")
    print("partition numbers into sign (1 bit), exponent(8 bit), mantisa (23 bit) (32 bits together) ")
    part = partition_number(s)
    print("Sign = " + part[0] + "\n" + "Exponent =  " + part[1] + "\n" + "Mantisa = " + part[2])
    print()

    print("Convert exponent to decimal and minus 127: ")
    exp = convert_bias(part[1])

    print("Exponent =  " + str(exp))
    print()
    print("Convert the mantisa to decimal:")
    mant = below_binary_to_decimal(part[2])
    print("Mantisa = " + str(mant))
    print()
    print("Convert to decimal using the equation: (-1)^s x (1+M) + 2^e")
    sign = int(part[0])
    print(ieee_equation(sign, exp, mant) + " = ")
    print(pow(-1, sign) * (1 + mant) * pow(2, exp))


convert("1100 0001 0101 1101 0000 0000 0000 0000")
