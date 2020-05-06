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
    print("Converting the integer part of the number:")
    init_number = number
    div = 2
    binary_string = ""
    while number != 0:
        print(str(number) + "/" + str(div) + " = " + str(number // div) + "    remainder = " + str(number % div))
        binary_string = str(number % div) + binary_string
        number = number // div
    print(str(init_number) + ", is " + binary_string + " in binary")
    return binary_string


def convert_decimal_to_bin(number):
    number = abs(number)
    return decimal_to_binary(float_splitter(number)[0]) + "." + convert_post_dot_to_bin(number)


def calculate_exponent(s):
    exp = len(s.split(".")[0]) - 1
    print("exponent = " + str(exp))

calculate_exponent("111.00")


def exponent_string_manipulate(s):
    s = s.split(".")
    s = s[0] + s[1]
    return s[0] + "." + s[1:]


def calculate_sign(i):
    return 1 if i < 0 else 0


def main():
    fract_bin = convert_decimal_to_bin(17.625)
    print(" ")
    print("Binary representation of the fractional decimal: ")
    print(fract_bin)


main()
