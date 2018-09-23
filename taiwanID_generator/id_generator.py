#!/usr/bin/python3
"""
Program:
    Generate a random Taiwan ID
Author:
    haw

Usage:
    id_generator.py

Error Code:
    1 - Program usage error
    11 - Personal ID format error
"""

import sys, re
import random
import logging_class as lgcl

LETTERS = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14,
           'F': 15, 'G': 16, 'H': 17, 'I': 34, 'J': 18,
           'K': 19, 'L': 20, 'M': 21, 'N': 22, 'O': 35,
           'P': 23, 'Q': 24, 'R': 25, 'S': 26, 'T': 27,
           'U': 28, 'V': 29, 'W': 32, 'X': 30, 'Y': 31,
           'Z': 33}

logger = lgcl.PersonalLog('id_generator')


def main():
    """
    USAGE:
        id_generator.py
    """
    checksum = 0
    personal_id = ''

    # Randomly choose a LETTER
    letter = random.choice(list(LETTERS))
    alpha_num = LETTERS[letter]
    checksum = (alpha_num // 10) + (alpha_num % 10) * 9
    personal_id += letter

    # Gender number
    gender = random.randint(1, 2)
    checksum += 8 * gender
    personal_id += str(gender)

    # Assigning numbers
    for multiplier in range(7, 0, -1):
        number = random.randint(0, 9)
        checksum += multiplier * number
        personal_id += str(number)
    personal_id += str(10 - (checksum % 10))

    # Result
    logger.info(personal_id)
    print('New ID: {}'.format(personal_id))



if __name__ == '__main__':
    main()
