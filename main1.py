print("main1")

from config import A
from config import B
from config import *

a = A()
print(A.apple, 100)
print(a)
print(a.apple)

print(B)
print(B['banana'])

print("main1")