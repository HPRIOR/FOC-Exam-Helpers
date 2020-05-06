def float_splitter(f):
    """
    float -> (int, int)
    """
    t = str(f).split('.')
    return int(t[0]), int(t[1])


def convert_post_dot_to_bin(f):
    print("")
    binary_string = ""
    after_dot = float("0." + str(float_splitter(f)[1]))
    print("The fractional part of the number is: " + str(after_dot))
    print("converting this to binary: ")
    while after_dot != 0:
        calc = after_dot * 2
        # split the outcome of after_dot*2
        split_float = float_splitter(calc)
        # add first half of binary to binary list
        binary_string += str(split_float[0])
        print(str(after_dot) + "x 2 = " + str(calc) + "      int remainder = " + str(split_float[0]))
        # make after dot post-dot part of new calc
        after_dot = float("0." + str(float_splitter(calc)[1]))
    return binary_string + "0"


def decimal_to_binary(number):
    init_number = number
    div = 2
    binary_string = ""
    while number != 0:
        print(str(number) + "/" + str(div) + " = " + str(number // div) + "    remainder = " + str(number % div))
        binary_string = str(number % div) + binary_string
        number = number // div
    print(str(init_number) + ", is " + binary_string + " in binary")
    print("")
    return binary_string


def convert_decimal_to_bin(number):
    number = abs(number)
    return decimal_to_binary(float_splitter(number)[0]) + "." + convert_post_dot_to_bin(number)


def exponent_string_manipulate(s):
    s = s.split(".")
    s = s[0] + s[1]
    return s[0] + "." + s[1:]


def getmantisa(s):
    return s.split(".")[1]


def calculate_exponent(s):
    exp = len(s.split(".")[0]) - 1
    print("")
    print("Find the exponent by moving up the decimal place: ")
    print(s + " becomes: " + exponent_string_manipulate(s))
    mantisa = getmantisa(exponent_string_manipulate(s))
    print("Therefore:")
    print("Mantisa = " + mantisa)
    print(" ")
    print("Exponent = " + str(exp))
    print("Add the bias to the exponent: ")
    exp_to_bin = exp + 127
    print(str(exp) + " + 127 = " + str(exp_to_bin))
    print("convert this to binary: ")
    print("")
    return decimal_to_binary(exp_to_bin), mantisa


def calculate_sign(i):
    return 1 if i < 0 else 0

def get_thirty_two_bit_mantisa(f):
    for i in range(23-len(f)):
        f = f + "0"
    return f

def split_into_groups_four(s):
    string_return = ""
    s = s[::-1]
    for index, ch in enumerate(s):
        if (index) % 4 == 0:
            string_return += " " + ch
        else:
            string_return += ch
    return string_return[::-1]

def main():
    num = float(input("insert floating point number:"))
    print("convert integer part of decimal to binary:")
    print("")
    fract_bin = convert_decimal_to_bin(num)
    print(" ")
    print("Binary representation of the fractional decimal: ")
    print(fract_bin)
    exponent_mantisa = calculate_exponent(fract_bin)
    sign = calculate_sign(num)
    print("the sign bit is: " + str(sign))
    print("the biased-exponent is: " + exponent_mantisa[0])
    mantisa = get_thirty_two_bit_mantisa(exponent_mantisa[1])
    print("the mantisa is: " + mantisa)
    print("therefore the 32 bit floating point IEEE format is: ")
    print(split_into_groups_four(str(sign) + exponent_mantisa[0] + mantisa))


main()
