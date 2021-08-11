from typing import Tuple
from math import floor

def eucext(a, b) -> Tuple[int, int, int]:
  x=s=1
  y=r=0
  g=a
  t=b

  while (t > 0):
    q = floor(g / t)
    u = x - q*r
    v = y - q*s
    w = g - q*t

    x=r; y=s; g=t
    r=u; s=v; t=w
  
  return (g, x, y)

def invmod(a, m) -> int:
  g, x, y = eucext(a, m)
  if g != 1:
    raise Exception('No inverse exists')
  else:
    return x % m