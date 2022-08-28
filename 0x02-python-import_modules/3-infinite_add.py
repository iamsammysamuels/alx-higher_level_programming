"""from sys import argv
if __name__ != "__main__":
    exit(0)
result = 0
argc = len(argv) - 1
i = 0
if argc != 0:
    for num in argv:
        if i != 0:
            result += int(num)
        else:
            i += 1
    print("{:d}".format(result))"""

#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

i = 0
result = 0
for argument in sys.argv:
    if i != 0:
        result += int(argument)
    else:
        i += 1
print("{:d}".format(result))
