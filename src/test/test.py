from simulator.utils import binaryUtils

if __name__ == '__main__':
    print(binaryUtils.to_binary_value(20+1))

    bin_str = binaryUtils.hex_to_bin('B')
    print(bin_str)
    print(int(bin_str, 2))

    print(int('011111111111', 2))
    switch = {
        'HLT': 0,
        'LDR': 1,
        'STR': 2,
        'LDA': 3,
        'LDX': 41,
        'STX': 42
    }
    value = switch['LDR']
    print(type(value))
    opcode = binaryUtils.to_binary_with_length(switch['LDR'], 6)
    r = '10'
    x = '00'
    i = '0'
    address = binaryUtils.to_binary_with_length('10', 5)

    instruction = opcode + r + x + i + address
    print(instruction)

    print(binaryUtils.bin_to_hex(instruction, 4))

