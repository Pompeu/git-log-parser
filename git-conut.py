#!/usr/bin/python3

import argparse
from FindBAseGit import FindBaseGit 
from Exec import Exec 

parser = argparse.ArgumentParser()

parser.add_argument('-init', action='store',
                    dest='init',
                    help='initial date of range')

parser.add_argument('-end', action='store',
                    dest='end',
                    help='end date of range')

parser.add_argument('-author', action='store',
                    dest='author',
                    help='set CKeyBB like Cnnnnnnnnnn')
parser.add_argument('-nw', action='store',
                    default='no',
                    dest='nw',
                    help='user yes or no for write files on disc')

parser.add_argument('-sort', action='store',
                    dest='sort',
                    default='no',
                    help='yes to sort, no to randon')

parser.add_argument('--version', action='version',
                    version='%(prog)s 1.0')

def parse_results(results):
    init = results.init
    end = results.end
    author = results.author
    nw = results.nw
    sort = results.sort
    base = FindBaseGit(init, end, author, nw, sort)

    if base.is_valid_params():
        exec_count = Exec(base)
        exec_count.start()

if __name__ == '__main__':
    results = parser.parse_args()
    print(results)
    parse_results(results)
