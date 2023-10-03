#!/usr/bin/python3

for num in range(0, 89):
    if (num % 10) <= (num // 10):
        continue
    print("{:02}".format(num), end=", ")
else:
    print(f"{num + 1}")
