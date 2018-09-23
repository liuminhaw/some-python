#!/usr/bin/python3
"""
Program:
    Check if an Taiwan id is valid
Author:
    haw

Usage:
    id_identifier.py PERSONAL_ID

Error Code:
    1 - Program usage error
    11 - Personal ID format error
"""

import sys, re
import logging_class as lgcl

LETTERS = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14,
           'F': 15, 'G': 16, 'H': 17, 'I': 34, 'J': 18,
           'K': 19, 'L': 20, 'M': 21, 'N': 22, 'O': 35,
           'P': 23, 'Q': 24, 'R': 25, 'S': 26, 'T': 27,
           'U': 28, 'V': 29, 'W': 32, 'X': 30, 'Y': 31,
           'Z': 33}

logger = lgcl.PersonalLog('id_identifier')


def main():
    message = \
    """
    USAGE:
        id_identifier.py PERSONAL_ID
    """
    checksum = 0

    # Check program usage
    try:
        personal_id = sys.argv[1]
    except IndexError:
        print(message)
        sys.exit(1)

    # Check personal id syntax
    re_pattern = re.compile(r'^[a-zA-Z][0-9]{9}')
    re_match = re_pattern.fullmatch(personal_id)

    if re_match == None:
        logger.warning('Personal ID format error.')
        sys.exit(11)

    # Alphabet number transform
    alpha_num = LETTERS[personal_id[0].upper()]
    checksum = (alpha_num // 10) + (alpha_num % 10) * 9

    multiplier = 8
    for num in personal_id[1:]:
        checksum += multiplier * int(num)
        multiplier -= 1
    checksum += int(personal_id[-1])

    # Result
    if checksum % 10 == 0:
        print('Valid personal ID')
    else:
        print('Invalid personal ID')


if __name__ == '__main__':
    main()
