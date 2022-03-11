from utils import binaryUtils

if __name__ == '__main__':
    a = [1,2,3]
    print(type(a) == list)

    s = '0000010203000000'
    print(len(s))
    print(s[0:6])
    print(s[6:8])
    print(s[8:10])
    print(s[10:11])
    print(s[11:])

    registers = {
        "gpr": {0: '0', 1: '', 2: '', 3: ''},
        "ix": {0: '0', 1: '', 2: '', 3: ''},
        "pc": '',
        "mar": '',
        'mbr': '',
        'ir': '',
        'mfr': '',
        'cc': '',
        "fr0": '',
        "fr1": ''
    }
    registers["gpr"][0] = "0"*16
    print(registers["gpr"][0])
    print(int('10'))

    address = 10
    address = address + int('0')
    #print(bin('10'))

    value = 33949
    value = binaryUtils.to_binary_with_length(value, 16)
    print(value)
    print(binaryUtils.to_binary_with_length(29, 16))
    ins = '1000010010101000'
    print(int(ins[0:6], 2))
    print(int('100001', 2))

    print(binaryUtils.hex_to_bin("84A8"))
    print(len("000001000011111101000"))
    print(int('1000'))

