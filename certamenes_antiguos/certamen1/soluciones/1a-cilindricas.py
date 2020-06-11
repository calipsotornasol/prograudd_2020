from math import sin, cos, pi
rho = float(input('Ingrese rho: '))
phi = float(input('Ingrese phi: '))
z = float(input('Ingrese z:' ))

phi = pi * phi/180

print(rho*cos(phi), rho*sin(phi), z)