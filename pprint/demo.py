import pprint
import re


def pprintDemo():
    varsList = [
        [1, 2, 3],
        ["ab", "c", "def"],
        re.compile("\w+"),
        ("123", "abc"),
        {
            "key1": "value1",
            "key2": "value2",
        }
    ]

    for value in varsList:
        print value

    print "-" * 80

    pp = pprint.PrettyPrinter(indent=4)
    for value in varsList:
        pp.pprint(value)

    print "=" * 80
    stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
    stuff.insert(0, stuff[:])
    print stuff
    print "-" * 80
    pp.pprint(stuff)


if __name__ == '__main__':
    pprintDemo()
