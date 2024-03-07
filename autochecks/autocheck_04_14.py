import sys


def parse_args():
    result = ""
    args = sys.argv
    args.pop(0)
    for arg in args:
        result = result + arg + " "

    result = result.rstrip()

    return result


print(parse_args())
