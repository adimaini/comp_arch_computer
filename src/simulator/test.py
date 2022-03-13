from utils import binaryUtils

if __name__ == '__main__':
    file_name = 'IPL.txt'
    f = open(file_name)
    line = f.readline()
    while line:
        if line[0] == '#' or line == '\n':
            line = f.readline()
            continue

        if line.find('#') != -1:
            end_index = line.find('#')
            line = line[0:end_index]

        line = line.strip('\n')
        strs = line.split("\t")
        address_bin_str = binaryUtils.hex_to_bin(strs[0])
        value_bin_str = binaryUtils.hex_to_bin(strs[1])

        print(line)
        #print(strs)
        # idx = int(address_bin_str, 2)
        # list[idx].value = int(value_bin_str, 2)

        line = f.readline()
    f.close()
