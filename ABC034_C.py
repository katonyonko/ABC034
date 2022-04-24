import io
from re import I
import sys

_INPUT = """\
6
4 3
123 456
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mod=10**9+7
  W,H=map(int,input().split())
  F=[1]
  N=W+H
  for i in range(N):
      F.append(F[-1]*(i+1)%mod)
  I=[pow(F[-1],mod-2,mod)]
  for i in range(N):
      I.append(I[-1]*(N-i)%mod)
  I=I[::-1]
  print(F[W+H-2]*I[W-1]*I[H-1]%mod)