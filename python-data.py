import re
import os
import sys

with open(os.path.join(sys.path[0], "real.txt"), "r") as f:
    x = f.read()

sequence = re.findall('[0-9]+',x)

print(sum([int(num) for num in sequence]))
