def partition_number(s):
    return s[0], s[1:9], s[9:32]


def convert_bias(s):
    return int(binary_to_decimal(s)) - 127


def binary_to_decimal(s):
    s = s[::-1]
    ans = 0
    for enum, i in enumerate(s):
        if i == "1":
            ans += pow(2, enum)
    return ans


def below_binary_to_decimal(s):
    ans = 0
    for enum, i in enumerate(s):
        if i == "1":
            ans += pow(2, -(enum + 1))
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

    sign = int(part[0])
    exp = convert_bias(part[1])
    mant = below_binary_to_decimal(part[2])
    print( "Exponent =  " + str(exp) )

    print("Mantisa = " + str(mant))
    return ieee_equation(sign, exp, mant)


print(convert("1100 0001 0101 1101 0000 0000 0000 0000"))
