#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    number = len(argv)
    if number == 1:
        print("0 arguments.")
    elif number == 2:
        print("1 argument:")
        for i in range(1, number):
            print("{}: {}".format(i, argv[i]))
    else:
        print("{} arguments:".format(number - 1))
        for i in range(1, number):
            print("{}: {}".format(i, argv[i]))
