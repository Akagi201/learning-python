
# python argparse3.py --verbose 1

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--verbose", help="increase output verbose")
args = parser.parse_args()

if args.verbose:
    print("verbose turned on")
