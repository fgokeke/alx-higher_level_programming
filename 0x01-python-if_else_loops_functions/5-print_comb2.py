#!/usr/bin/python3
for no in range(0, 100):
    if no == 99:
        print("{}".format(no))
    else:
        print("{:02}".format(no), end=", ")
