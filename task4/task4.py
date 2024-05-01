import os.path
import sys
from re import findall


try:
    with open(os.path.join((sys.argv[1]))) as file:
        nums_list = list(map(int, findall(r'[+-]?\d+', file.read())))

except OSError:
    print("OS Error")

else:
    # The median is the middle element of the array after sorting it.
    median = sorted(nums_list)[len(nums_list) // 2]
    result = 0
    for number in nums_list:
        result += abs(median - number)
    print(result)
