
# python argparse5.py -v / --verbose

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v","--verbose", help="increase output verbose", action="store_true")
args = parser.parse_args()

if args.verbose:
    print("verbose turned on")
