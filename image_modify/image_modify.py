#!/usr/bin/python
#
# Program:
#     Compress jpeg image file
# Author:
#     haw

import sys, os
from PIL import Image

import logging_class


FILETYPE = ('.jpg', '.jpeg')


class Directory():

    def __init__(self,path):
        self.abs = os.path.abspath(path)
        self.dir = os.path.abspath(path)
        self.base = path


class File(Directory):

    def __init__(self, path):
        Directory.__init__(self, path)

        self.dir = os.path.dirname(self.abs)
        self.base = os.path.basename(self.abs)
        self.file_name = os.path.splitext(self.base)[0]
        self.file_extension = os.path.splitext(self.base)[1]



def main():
    message = \
    """
    USAGE:
        image_modify compress INPUTFILE OUTPUTDIR [QUALITY]
    """
    if len(sys.argv) < 4:
        print(message)
        sys.exit(1)
    elif sys.argv[1] == 'compress':
        image_compress()
    else:
        print(message)


def image_compress():
    message = \
    """
    USAGE:
        image_modify compress INPUTFILE OUTPUTDIR [QUALITY]
    NOTE:
        Use . for OUPUTDIR to indicate current directory
        QUALITY should be between 1 to 95
        Default value is 75 if not specified
    """
    logger = logging_class.PersonalLog("image_proc")

    # Input validation
    try:
        input_file = File(sys.argv[2])
        output_dir = Directory(sys.argv[3])
    except IndexError:
        print(message)
        sys.exit(1)

    # Test if input file exist
    if not os.path.isfile(input_file.abs):
        logger.warning('Source file {} does not exist.'.format(input_file.abs))
        sys.exit(1)

    # Test if image is jpg file
    if input_file.file_extension.lower() not in FILETYPE:
        print('Image should be jpeg format')
        sys.exit(1)

    # Test if output directory exist
    if output_dir.base == '.':
        output_dir.abs = os.getcwd()
        output_dir.dir = os.getcwd()
    elif not os.path.isdir(output_dir.dir):
        logger.warning('Destination directory {} does not exist.'.format(output_dir.dir))
        sys.exit(1)

    # Test quality value
    try:
        compress_quality = int(sys.argv[4])
        if compress_quality < 1 or compress_quality > 95:
            raise Warning
    except ValueError:
        print('QUALITY should be numeric value.')
        sys.exit(1)
    except Warning:
        print('QUALITY value should be between 1 to 95.')
        sys.exit(1)
    except:
        compress_quality = 75

    # Compress image
    new_filename = input_file.file_name+'-Compressed'+input_file.file_extension
    output_file = File(os.path.join(output_dir.dir, new_filename))

    try:
        with Image.open(input_file.abs) as image_file:
            image_file.save(output_file.abs, quality=compress_quality)
        logger.info('Compress image {} success'.format(input_file.abs))
    except:
        logger.warning('Failed to compress image {}'.format(input_file.abs))
        sys.exit(1)


if __name__ == '__main__':
    main()
