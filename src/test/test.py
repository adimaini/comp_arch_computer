from simulator.utils import binaryUtils


if __name__ == '__main__':
    print(binarayUtils.to_binary_value(20))

    bin_str = binarayUtils.hex_to_bin('B')
    print(bin_str)
    print(int(bin_str, 2))

    print(int('011111111111', 2))

    for i in range(1,10):
        print(i)