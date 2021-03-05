import os
import sys

name = sys.argv[1] if len(sys.argv) > 1 else ""
python = "pypy3"

for letter in "abcdef":
    os.system(f"{python} run.py {letter} {name}")