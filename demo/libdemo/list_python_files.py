import sys
import os

if len(sys.argv) > 1:
    top = sys.argv[1]
else:
    top = '.'  # current directory

for (dirname, directories, files) in os.walk(top):
    for f in files:
        if f.endswith(".py"):
            print(dirname + "\\" + f)
