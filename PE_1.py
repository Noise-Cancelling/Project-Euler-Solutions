# Project Euler, 1
# Justin Starrett 2021

result = 0

for i in range(0, 1000):
    if (i % 3 == 0) or (i % 5 == 0):
        print(i)
        result += i
print(result)
