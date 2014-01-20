import sys

def sumOfDigits():
    fname = sys.argv[1]
    numList = map(lambda x: int(x.strip()), open(fname).readlines())
    for num in numList:
        n = num
        sum = 0
        while n > 0:
            sum = sum + (n % 10)
            n = n / 10
        print sum
        
if __name__ == "__main__":
    sumOfDigits()