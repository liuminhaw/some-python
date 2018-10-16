#!/usr/bin/python3
"""
Program:
    Backup password for lastpass to files
Author:
    haw

Usage:
    lastpass_backup.py DESTINATION_DIRECTORY

Error Code:
    1 - Program usage error

    11 - Destination directory not exist
"""


import sys, os
import getpass

import block_class as blkcl
import logging_class as lgcl

logger = lgcl.PersonalLog('lastpass_backup')


class PasswordInfo():

    def __init__(self, site, user, password, url):
        self.site = site
        self.username = user
        self.password = password
        self.site_url = url


def main():
    message = \
    """
    USAGE:
        lastpass_backup.py DESTINATION_DIRECTORY
    """

    # Check program syntax usage
    try:
        output_dir = blkcl.Directory(sys.argv[1])
    except IndexError:
        print(message)
        sys.exit(1)

    # Check directory existence
    if not output_dir.dir_exist():
        logger.info('Target directory {} not exist.'.format(ourput_dir.dir))
        sys.exit(11)

    # Password file creation
    print('Press CTRL-C to exit.\n')

    while True:
        try:
            # Get password information
            information = _request_info()
            # Write to file
            _password_backup(information, output_dir.dir)
        except FileExistsError:
            continue
        except KeyboardInterrupt:
            print('\nlastpass_backup exit.')
            sys.exit(0)



def _request_info():
    """
    Get password information from user
    Return:
        PasswordInfo object
    """
    site, username, password, url = '', '', '', ''

    while site =='':
        site = input('Site: ')
    while username == '':
        username = input('User name: ')
    while password == '':
        password = getpass.getpass('Password: ')
    while url == '':
        url = input('URL: ')

    return PasswordInfo(site, username, password, url)


def _password_backup(info, path):
    """
    Backup password informations

    Error:
        FileExistsError - Raise if file already exist
        KeyboardInterrupt - Raise when Ctrl-C is pressed
    """

    new_file = blkcl.File(os.path.join(path, info.site))

    # Check file existence
    if new_file.file_exist():
        logger.info('File {} already exist.'.format(new_file.abs))
        raise FileExistsError

    # Write file
    try:
        with open(new_file.abs, mode='wt', encoding='utf-8') as file:
            file.write('SITE NAME: {}\n'.format(info.site))
            file.write('USERNAME: {}\n'.format(info.username))
            file.write('PASSWORD: {}\n'.format(info.password))
            file.write('SITE URL: {}\n'.format(info.site_url))
    except KeyboardInterrupt:
        if new_file.file_exist():
            os.remove(new_file.abs)
        raise KeyboardInterrupt

    print('Create file {} success.\n'.format(new_file.abs))



if __name__ == '__main__':
    main()
