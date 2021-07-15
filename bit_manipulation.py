"""
how to manipulate bit, and bitwise operations
&, |, <<, >>, ^
bin(0 << 1) if all bits are zeros, left shift will always still 0
bin(1 << 1) will shift 1 to left: 0001 -> 0010
bin(0 & 1) = 0
bin(1 | 0) = 1
"""


# 1. reverse all bits for 32-bit integer
# for example: (43261596) 00000010100101000001111010011100  reverse to (964176192) 00111001011110000010100101000000
def bit_reverse(n):
    result = 0
    for i in range(32):
        result = result << 1
        result = result | (n & 1)
        n = n >> 1
    return result



if __name__ == "__main__":
    n = 43261596
    print(bit_reverse(n))