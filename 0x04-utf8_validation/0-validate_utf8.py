#!/usr/bin/python3
"""UTF-8 Encoding"""


def validUTF8(data):
    """Method that determines if a given data set represents
       a valid utf-8 encoding
    """
    num_bytes = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for n in data:

        mask_bytes = 1 << 7

        if num_bytes == 0:

            while mask_bytes & n:
                num_bytes += 1
                mask_bytes = mask_bytes >> 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            if not (n & mask1 and not (n & mask2)):
                return False

        num_bytes -= 1

    if num_bytes == 0:
        return True

    return False
