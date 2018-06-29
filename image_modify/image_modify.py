#!/usr/bin/python

"""
# Program:
#    Make simple image modification
# Author
#    haw
# Exit Code:
#    13 - Fail _input_check
#    15 - Fail _file_exist_check
#    17 - Fail _file_format_check
#    19 - Fail _directory_exist_check
#
#    3 - Fail image_compress
#    4 - Fail image_resize
"""

import sys, os
from PIL import Image

import logging_class


FILETYPE = ('.jpg', '.jpeg', '.png')

logger = logging_class.PersonalLog('image_modify')


class Directory():

    def __init__(self,path):
        self.abs = os.path.abspath(path)
        self.dir = os.path.abspath(path)
        self.base = path

    def dir_exist(self):
        return os.path.isdir(self.dir)


class File(Directory):

    def __init__(self, path):
        Directory.__init__(self, path)

        self.dir = os.path.dirname(self.abs)
        self.base = os.path.basename(self.abs)
        self.file_name = os.path.splitext(self.base)[0]
        self.file_extension = os.path.splitext(self.base)[1]

    def file_exist(self):
        return os.path.isfile(self.abs)




def main():
    message = \
    """
    USAGE:
        image_modify compress INPUTFILE OUTPUTFILE [QUALITY]
        image_modify resize INPUTFILE OUTPUTFILE [PROPORTION]
    """
    if len(sys.argv) == 1:
        print(message)
        sys.exit(1)
    elif sys.argv[1] == 'compress':
        image_compress()
    elif sys.argv[1] == 'resize':
        image_resize()
    else:
        print(message)


def image_compress():
    message = \
    """
    USAGE:
        image_modify compress INPUTFILE OUTPUTFILE [QUALITY]
    NOTE:
        QUALITY should be between 1 to 95
        Default value is 75 if not specified
    """
    FILETYPE = ('.jpg', '.jpeg')

    # Input validation
    input_file, output_file = _input_check(message)

    # Test if input file exist
    _file_exist_check(input_file)

    # Test if image is jpg file
    _file_format_check(input_file, FILETYPE)

    # Test if output directory exist
    _directory_exist_check(output_file)

    # Test quality value
    try:
        compress_quality = int(sys.argv[4])
        if compress_quality < 1 or compress_quality > 95:
            raise Warning
    except ValueError:
        print('QUALITY should be numeric value.')
        sys.exit(3)
    except Warning:
        print('QUALITY value should be between 1 to 95.')
        sys.exit(3)
    else:
        compress_quality = 75

    # Compress image
    try:
        with Image.open(input_file.abs) as image_file:
            image_file.save(output_file.abs, quality=compress_quality)
        logger.info('Compress image {} success'.format(input_file.abs))
    except:
        logger.warning('Failed to compress image {}'.format(input_file.abs))
        sys.exit(3)


def image_resize():
    message = \
    """
    USAGE:
        image_modify resize INPUTFILE OUTPUTFILE [PROPORTION]
    NOTE:
        PROPORTION will devide the origin image width and height by the value
        Default value for PROPORTION is 2 if not specified
    """

    # Input validation
    input_file, output_file = _input_check(message)

    # Test input file
    _file_exist_check(input_file)

    # Test file format
    _file_format_check(input_file)

    # Test output directory
    _directory_exist_check(output_file)

    # Test proportion
    try:
        proportion = int(sys.argv[4])
        if proportion <= 0:
            raise Warning
    except ValueError:
        logger.warning('PROPORTION should be numeric value.')
        sys.exit(4)
    except Warning:
        logger.warning('PROPORTION should be positive integer.')
        sys.exit(4)
    except:
        proportion = 2

    # Resize image
    try:
        with Image.open(input_file.abs) as image_file:
            width, height = image_file.size
            new_image_file = image_file.resize((width // proportion, height // proportion))
            new_image_file.save(output_file.abs, quality=100)
            logger.info('Resize image {} success.'.format(input_file.abs))
    except:
        logger.warning('Failed to resize image {}.'.format(input_file.abs))
        sys.exit(4)



def _input_check(message):
    """
    Check program input arguments

    Input:
        message - string
    """

    try:
        input_file = File(sys.argv[2])
        output_file = File(sys.argv[3])
    except IndexError:
        print(message)
        sys.exit(13)

    return (input_file, output_file)


def _file_exist_check(file):
    """
    Check input file existence

    Input:
        file - File class object
    """

    if not file.file_exist():
        logger.warning('Source file {} does not exist.'.format(file.abs))
        sys.exit(15)


def _directory_exist_check(file):
    """
    Check output directory existence

    Input:
        dir - File class object
    """

    if not file.dir_exist():
        logger.warning('Destination directory {} does not exist.'.format(dir.dir))
        sys.exit(19)


def _file_format_check(file, formats=('.jpg','.jpeg','.png')):
    """
    Check input file format

    Input:
        file - File class object
        formats - tuple of file format
    """

    if file.file_extension.lower() not in formats:
        logger.info('Source file format not in {}.'.format(' '.join(formats)))
        sys.exit(17)



if __name__ == '__main__':
    main()
