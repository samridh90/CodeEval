import os
from sys import argv

def printFileSize():
    fpath = argv[1]
    print os.stat(fpath).st_size
    

if __name__ == "__main__":
    printFileSize()