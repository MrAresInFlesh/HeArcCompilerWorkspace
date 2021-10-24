import re


def checkIfRealNumber(number):
    realNumber = re.compile(r"^[-+]?[0-9]*\.?[0-9]+(e[-+]?[0-9]+)?$")
    print(realNumber)


if __name__ == '__main__':
    checkIfRealNumber('4')
