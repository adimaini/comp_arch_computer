from utils import binaryUtils

if __name__ == '__main__':

    #print(int('0000 1010 0000 1111', 2))
    print(binaryUtils.to_binary_with_length(-1, 16))

    s = binaryUtils.hex_to_bin('0102')
    print(int(s,2))

    s = binaryUtils.hex_to_bin('CB01')
    number_func_dict = {
        '1': 'LDR', '2': 'STR', '3': 'LDA', '41': 'LDX', '42': 'STX',
        '10': 'JZ', '11': 'JNE', '12': 'JCC', '14': 'JSR', '15': 'RFS', '16': 'SOB',
        '17': 'JGE',
        '4': 'AMR', '5': 'SMR', '6': 'AIR', '7': 'SIR', '20': 'MLT', '21': 'DVD', '22': 'TRR',
        '23': 'AND', '24': 'ORR', '25': 'NOT', '31': 'SRC', '32': 'RRC',
        '61': 'IN', '62': 'OUT', '63': 'CHK'
    }
    
    opcode = number_func_dict[oct(int(s[0:6], 2))[2:]]
    r = int(s[6:8], 2)
    x = int(s[8:10], 2)
    i = int(s[10:11], 2)
    address = int(s[11:], 2)

    print('%s, %i, %i, %i, %i' % (opcode, r, x, address, i))


