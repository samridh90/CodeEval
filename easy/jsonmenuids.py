from sys import argv
import json


def sumOfIds(obj):
    arr = obj['menu']['items']
    sum = 0
    for item in arr:
        if item and 'label' in item:
            sum += item['id']
    return sum


if __name__ == '__main__':
    tests = open(argv[1])
    for test in tests:
        test = json.loads(test)
        print sumOfIds(test)
    tests.close()
