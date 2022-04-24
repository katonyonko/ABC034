import io
import sys

_INPUT = """\
6
3 2
100 15
300 20
200 30
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,K=map(int,input().split())
  youki=[list(map(int,input().split())) for _ in range(N)]
  l,r=0,101
  for i in range(100):
    mid=(l+r)/2
    tmp=[youki[j][0]*(youki[j][1]-mid) for j in range(N)]
    tmp.sort(reverse=True)
    if sum(tmp[:K])>=0: l=mid
    else: r=mid
  print(l)