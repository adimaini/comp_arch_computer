from utils import binaryUtils

if __name__ == '__main__':

    s = binaryUtils.hex_to_bin('3037')
    print(s)
    print(s[0:6])
    print(oct(int(s[0:6], 2)))
    print(s[6:8])
    print(s[8:10])
    print(s[10:11])
    print(s[11:])
    print(len('0000 0001 0000 0000'))
    print(binaryUtils.to_binary_with_length(int('0100', 16), 16))
    print(int('0000000100000000',2))
