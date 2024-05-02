import sys


n, m = int(sys.argv[1]), int(sys.argv[2])
round_array = [i for i in range(1, n + 1)]
result = ''

while True:
    result += str(round_array[0])
    for _ in range(m - 1):
        round_array.append(round_array.pop(0))
    if round_array[0] == 1:
        print(''.join(result))
        break
