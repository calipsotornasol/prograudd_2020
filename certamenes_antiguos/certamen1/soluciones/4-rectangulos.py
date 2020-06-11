from math import sin, pi

area = 0
for i in range(1000):
    y = 100 * sin(pi * i / 1000)
    area = area + i*y
    
print(area)