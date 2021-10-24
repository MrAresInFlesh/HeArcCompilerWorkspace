import re
import sys


def flt(filename, var):
    regex = re.compile(sys.argv[1])
    with open(filename) as f:
        for line in [line for line in f if regex.search(line)]:
            print(line)


if __name__ == '__main__':
    flt(sys.argv[2], sys.argv[1])
