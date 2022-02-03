# comp_arch_computer
Class project for Computer Architecture course with Morris Lancaster

# The naming rules are as follows:
- button : btn_xxxx
- lable: lbl_xxx
- lineEdit: le_xxx
- tableView: tb_xxx
# if we want to fold some code:
```python
#<editor-fold desc="description">
'''
 your code
'''
#</editor-fold>

```

# For the format of IPL.txt
```text
    0006 0001
    0007 0002
    0008 0004
    0009 0005
    000A 000B
    000B LDR
    000C STR
    000D HALT

Use 4 hexadecimal digits to represent 16-bit binary numbers
So, for number value, the first 4 bit represents the address and the last 4 bit represents the number
For the instruction, the first 4 bit represents the address, 
and 'LDR ...' represents a instruction that needs to decode into binary value.

```