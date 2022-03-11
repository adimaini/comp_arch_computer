# convert a decimal number to a length-bit binary string
def to_binary_with_length(value: int, length: int):
    '''
    :param value: int
    :param length: int
    :return:
    '''
    # print(value,length)
    bin_str = str(bin(value))[2:]
    res = '0' * (length - len(bin_str)) + bin_str
    return res


# convert a decimal number to a 16-bit binary string
def to_binary_value(value):
    return to_binary_with_length(value, 16)


# convert a hex-number-string to a 160bit binary string
def hex_to_bin(value):
    bin_str = str(bin(int(value, 16)))[2:]
    res = '0' * (16 - len(bin_str)) + bin_str
    return res
