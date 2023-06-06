#!/usr/bin/python3
n = 0
while n < 100:
    print("{:02d}".format(n), end="")
    n += 1
    if n < 100:
        print(", ", end="")
    else:
        print()
