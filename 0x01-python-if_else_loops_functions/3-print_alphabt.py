#!/usr/bin/python3
for ascii_value in range(ord('a'), ord('z') + 1):
    if chr(ascii_value) != 'q' and chr(ascii_value) != 'e':
        print("{}".format(chr(ascii_value)), end='')
