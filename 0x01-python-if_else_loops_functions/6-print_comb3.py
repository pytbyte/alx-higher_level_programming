#!/usr/bin/python3
for n1 in range(10):
    for n2 in range(n1 + 1, 10):
        print("{:02d}, ".format(n1 * 10 + n2), end="")

