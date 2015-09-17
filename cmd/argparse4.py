
# python argparse4.py --verbose

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--verbose", help="increase output verbose", action="store_true")
args = parser.parse_args()

if args.verbose:
    print("verbose turned on")
