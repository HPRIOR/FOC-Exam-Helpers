def split_into_groups_four(s):
    string_return = ""
    s = s[::-1]
    for index, ch in enumerate(s):
        if (index) % 4 == 0:
            string_return += " " + ch
        else:
            string_return += ch
    return string_return[::-1]


def undo_split_binary(s):
    l = s.split(" ")
    r = ""
    for el in l:
        r += el
    return r


def decimal_to_binary(number):
    print("convert absolute value of -" + str(number) + " to binary")
    init_number = number
    div = 2
    binary_string = ""
    while number != 0:
        print(str(number) + "/" + str(div) + " = " + str(number // div) + "    remainder = " + str(number % div))
        binary_string = str(number % div) + binary_string
        number = number // div
    print(str(init_number) + ", is " + split_into_groups_four(binary_string) + " in binary")
    return binary_string


def calc_remainder(val1, val2):
    return 1 if int(val1) + int(val2) == 2 else 0


def calc_answer(val1, val2):
    return 1 if int(val1) + int(val2) == 1 else 0


def convert_remainder(s):
    ret_string = ""
    for enum, char in enumerate(s):
        if enum == len(s) - 1:
            ret_string = ret_string + " "
        else:
            if char == "0":
                ret_string = ret_string + " "
            else:
                ret_string = ret_string + char
    return ret_string


def binary_add_one(s):
    #s = "0000" + s
    remainder_string = ""
    answer_string = ""
    line_string = "-"
    add_one_string = "1"

    remainder = str(calc_remainder(s[-1], 1))
    answer = str(calc_answer(s[-1], 1))
    remainder_string = remainder
    answer_string = answer

    count = len(s) - 2
    while count > -1:
        answer = calc_answer(s[count], remainder)
        answer_string = str(answer) + answer_string
        remainder = calc_remainder(s[count], remainder)
        remainder_string = str(remainder) + remainder_string
        line_string += "-"
        add_one_string = " " + add_one_string
        count -= 1

    print(convert_remainder(remainder_string))
    print(answer_string)
    print(line_string)
    print(s)
    print(add_one_string)
    return answer_string


def bit_flip(s):
    ret_s = ""
    for char in s:
        if char == "1":
            ret_s += "0"
        if char == "0":
            ret_s += "1"
    return ret_s


def make_thirty_two_bit_unsigned(s):
    add = ""
    for i in range(32 - len(s)):
         add += "0"
    return add + s

def decimal_to_twos_comp_binary():
    convert = input("Enter negative decimal to convert to twos compliment: ")
    print(" ")
    binary_string = decimal_to_binary(abs(int(convert)))
    print("")

    print("Make into a 32-bit unsigned integer")
    binary_string = make_thirty_two_bit_unsigned(binary_string)
    print(binary_string)
    print("")
    print("Flip the bits:")
    binary_string = bit_flip(binary_string)
    print(binary_string)
    print("")
    print("Add add one to the binary number:")
    binary_string = binary_add_one(binary_string)
    print("")
    print("The answer is", split_into_groups_four(binary_string))


decimal_to_twos_comp_binary()
