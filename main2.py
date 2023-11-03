print("main2")

import config

print(config.A)
print(config.B)

a = config.A()
print(config.A.apple, 100)
print(type(config.A.apple), 200)
print(type(config.A().apple), 300)
print(config.A().apple, 100)
print(a)
print(a.apple)

B = config.B
print(B)
print(B['banana'])
print("main2")