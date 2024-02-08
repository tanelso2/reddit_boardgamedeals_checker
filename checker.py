#!/usr/bin/env python3.6
import logging
import os
import argparse
from checker.checkers.boardgamedeals import BoardGameChecker


logging.basicConfig(level=logging.DEBUG)
mydir = os.path.abspath(os.path.dirname(__file__))

parser = argparse.ArgumentParser()
parser.add_argument('--config-dir', default=mydir)
parser.add_argument('--db-file', default=os.path.join(mydir, 'checker.db'))
args = parser.parse_args()

def main():
    checker = BoardGameChecker(args.db_file, args.config_dir)
    checker.check_submissions()

if __name__ == '__main__':
    main()
