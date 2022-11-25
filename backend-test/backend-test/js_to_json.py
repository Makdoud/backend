from data import data

import argparse

import os
import sys

# Create the parser
my_parser = argparse.ArgumentParser(description='This program has to filter a list of elements containing a pattern.')

# Add the arguments
my_parser.add_argument('--filter',
                       metavar='Filter',
                       type=str,
                       help='the filter')
my_parser.add_argument('--count',
                       metavar='Count',
                       type=str,
                       help='the counts of People and Animals by counting the number of children')


# Execute the parse_args() method
args = my_parser.parse_args()
filter= args.filter
count = args.count


lst =[]

def filtering(filter):
    for dico in data:
        if filter in dico['name']:
            lst.append(dico)
        else:
            for dict in dico['people']:
                if filter in dict['name']:
                    lst.append(dico)
                else:
                    for animal in dict['animals']:
                        if filter in animal['name']:
                            lst.append(dico)
    return lst