# convert a decimal number to a length-bit binary string
def to_binary_with_length(value, length):
    bin_str = str(bin(int(value)))[2:]
    res = '0' * (length - len(bin_str)) + bin_str
    return res


# convert a decimal number to a 16-bit binary string
def to_binary_value(value):
    return to_binary_with_length(value, 16)


# convert a hex-number-string to a 16bit binary string
def hex_to_bin(value):
    bin_str = str(bin(int(value, 16)))[2:]
    res = '0' * (16 - len(bin_str)) + bin_str
    return res

def bin_to_hex(value, length):
    hex_str = hex(int(value, 2))[2:]
    res = '0' * (length - len(hex_str)) +hex_str
    return res

