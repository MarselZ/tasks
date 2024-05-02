import os.path
import sys
from re import findall


re_pattern = r'[-+]?(?:(?:\d*\.\d+)|(?:\d+\.?))(?:[Ee][+-]?\d+)?'
with (open(os.path.join((sys.argv[1]), 'circle.txt')) as f1,
      open(os.path.join((sys.argv[2]), 'dot.txt')) as f2):
    x0, y0, r = map(float, findall(re_pattern, f1.read()))
    input_dots = findall(re_pattern, f2.read())
    dots = [(float(input_dots[i]), float(input_dots[i+1])) for i in range(0, len(input_dots), 2)]

# In order not to extract the root (because this is a more expensive operation, and
# the root may also be an irrational number), we will compare the squares of the radii.
r_sq = r**2
for dot in dots:
    rd_sq = (dot[0] - x0)**2 + (dot[1] - y0)**2
    if rd_sq == r_sq:
        print(0)
    elif rd_sq < r_sq:
        print(1)
    elif rd_sq > r_sq:
        print(2)
    else:
        print('SOMETHING WRONG!')
