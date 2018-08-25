"""
Program:
    Extract url from a text file.
Author:
    haw

Error Code:
    1 - Program usage error
    3 - Read input file IO Error

    11 - Input file existence error
    13 - Output file existence error
    15 - File extension type error
"""

import sys, re
import html, collections, hashlib

import logging_class as lgcl
import block_class as blkcl


logger = lgcl.PersonalLog('url_extractor')

URL_REGEX = r'((http)(s)?(\S)*(\.jpg|\.jpeg|\.png))'
FILE_FORMATS = ('.txt')


def main():
    message = \
    """
    USAGE:
        url_extractor.py INPUTFILE OUTPUTFILE
    """
    global FILE_FORMATS

    # Check input arguments
    try:
        input_file = blkcl.File(sys.argv[1])
        output_file = blkcl.File(sys.argv[2])
    except IndexError:
        print(message)
        sys.exit(1)

    # Check input and output file existence
    if not input_file.file_exist():
        logger.warning("Input file {} not exist.".format(input_file.abs))
        sys.exit(11)

    if output_file.file_exist():
        logger.info("Output file {} already exist.".format(output_file.abs))
        sys.exit(13)

    # Check input and output file format
    if not input_file.format_check(FILE_FORMATS):
        logger.warning("Input file not one of {} format.".format(FILE_FORMATS))
        sys.exit(15)

    if not output_file.format_check(FILE_FORMATS):
        logger.warning("Output file not one of {} format.".format(FILE_FORMATS))
        sys.exit(15)

    # Extract urls from input file
    urls_dict = _url_extract(input_file)
    print(urls_dict.values())

    # Write urls to output file
    with open(output_file.abs, mode='wt', encoding='utf-8') as write_file:
        for url in urls_dict.values():
            write_file.write('{}\n'.format(url))
            print('Write {} to file {} success.'.format(url, output_file.abs))



def _url_extract(file):
    """
    Find all urls from file,
    return an ordered dict containing all urls.

    Input:
        file - Block class File object
    """
    global URL_REGEX
    url_regex = re.compile(URL_REGEX, re.IGNORECASE)

    # Extract urls from file
    try:
        with open(file.abs, mode='rt', encoding='utf-8') as read_file:
            content = read_file.read()
            content = html.unescape(content)
            urls = url_regex.findall(content)
    except IOError as err:
        logger.warning('Read File IOError {}: {}'.format(err.errno, err.strerror))
        sys.exit(3)

    # Store urls into ordered dict
    urls_dict = collections.OrderedDict()
    for url in urls:
        hash_val = hashlib.sha256(url[0].encode()).hexdigest()
        hash_val = hash_val[:10]
        urls_dict[hash_val] = url[0]

    return urls_dict



if __name__ == '__main__':
    main()
