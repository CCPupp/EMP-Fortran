# A short utility to calculate the Dawson Integral using Python libraries.
# Last compiled and run on Ubuntu Linux. Uses Python 3. Requires Scipy to be installed
# From Terminal, type "sudo apt-get install python-scipy" before running for the first time.
import sys
from scipy import special

def run():
    x = round(float(sys.argv[1]))
    return special.dawsn(x)

if __name__ == "__main__":
    print("Begin")
