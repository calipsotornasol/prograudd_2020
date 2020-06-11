from math import sin, cos, pi
r = float(input('Ingrese r: '))
theta = float(input('Ingrese theta: '))
phi = float(input('Ingrese phi:' ))

theta = pi * theta/180
phi = pi * phi/180

print(r*sin(theta)*cos(phi), r*sin(theta)*sin(phi), r*cos(theta))