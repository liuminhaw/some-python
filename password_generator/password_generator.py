#! /usr/bin/python3

"""
USAGE:
    password_generator [length=LENGTH] [symbols]
NOTE:
    Default LENGTH is 15 if not defined
    Password will contain symbol character if given the option
AUTHOR:
    haw
"""

import sys, random, re, string
import logging
import logging_class

logging.disable(logging.DEBUG)

class Password:
    def __init__(self, length, specialChar):
        self.length = length
        self.choice = string.ascii_letters + string.digits
        self.password = ''

        if specialChar:
            self.choice += '`~!@#$%^&*()_-+={}[]\|:;"\'<>,.?/'

    def set_password(self):
        for i in range(self.length):
            self.password += random.choice(self.choice)

    def get_choice(self):
        return self.choice

    def get_length(self):
        return self.length

    def get_password(self):
        return self.password


def main():
    message = \
    """
    USAGE:
        password_generator [length=LENGTH] [symbols]
    """
    # Logging definition
    logger = logging_class.PersonalLog(sys.argv[0])

    # Default setting
    length = 15
    symbol = False

    # Command input recognition
    re_length = re.compile(r'^length=(\d+)$', re.IGNORECASE)
    re_symbol = re.compile(r'symbols', re.IGNORECASE)
    for option in sys.argv:
        if re_symbol.search(option) != None:
            symbol = True
        re_match = re_length.search(option)
        if re_match != None:
            length = int(re_match.group(1))

    logger.debug('Symbol Status: {}'.format(symbol))
    logger.debug('Length: {}'.format(length))

    # Generate password
    user_password = Password(length, symbol)
    user_password.set_password()

    # Write password to text file PasswordGenerated.txt
    with open('PasswordGenerated.txt', 'w') as write_file:
        write_file.write(user_password.password + '\n')
    logger.debug('Password: {}'.format(user_password.password))
    print('Write new generated password to PasswordGenerated.txt.')


if __name__ == "__main__":
    main()
