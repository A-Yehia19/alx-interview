#!/usr/bin/python3
"""Log parsing"""

import re


# global vars
fileSize = 0
statusCodes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}

def parse_input(line):
    '''Parses the input line'''
    parsers = [
        '(?P<ip>[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)',
        '(?P<date>.*)',
        '(?P<request>.*)',
        '(?P<status_code>[0-9]+)',
        '(?P<file_size>[0-9]+)'
    ]
    log_fmt = '^{} \\- \\[{}\\] \\"{}\\" {} {}$'.format(parsers[0], parsers[1], parsers[2], parsers[3], parsers[4])
    match = re.fullmatch(log_fmt, line)

    result = {}
    if match is not None:
        result['status_code'] = match.group('status_code')
        result['file_size'] = int(match.group('file_size'))
    return result

def update_values(line_info):
    '''Updates the values of the global variables'''
    global fileSize, statusCodes

    fileSize += line_info['file_size']
    if line_info['status_code'] in statusCodes:
        statusCodes[line_info['status_code']] += 1

def print_stats():
    '''Prints the statistics of the log.'''
    print('File size: {:d}'.format(fileSize), flush=True)
    for status_code in sorted(statusCodes.keys()):
        num = statusCodes.get(status_code, 0)
        if num > 0:
            print('{:s}: {:d}'.format(status_code, num), flush=True)


def main_run():
    """the main program to run"""
    line_num = 0
    try:
        while True:
            line = input()
            update_values(parse_input(line))
            line_num += 1
            if line_num % 10 == 0:
                print_stats()
    except (KeyboardInterrupt, EOFError):
        print_stats()
    

if __name__ == '__main__':
    """main program"""
    main_run()
