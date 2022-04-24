import io
import sys

_INPUT = """\
6
100
123456789
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  n=int(input())
  if n%2==0: print(n-1)
  else: print(n+1)