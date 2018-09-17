from time import sleep
import sys

# Asim's Awesome Idea
def tprint(string):
    for c in string:
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(0.025)
    print('')