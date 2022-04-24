import io
import sys

_INPUT = """\
6
12 34
98 56
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  x,y=map(int,input().split())
  if x<y: print('Better')
  else: print('Worse')