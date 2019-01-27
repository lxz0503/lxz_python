#!/usr/bin/env python
#encoding=UTF-8
import re
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--log',
			dest='log',
			default='',
			help='name of the MEFA L4 original log',
			metavar='')
    parser.add_argument('--version',
			dest='version',
			default='',
			help='IP version and prefix of CSV',
			metavar='')
    input = parser.parse_args()
    print type(input)
    print input.log
    print input.version
