def real_imag_conj(val):
    return val.real, val.imag, val.conjugate()

r= real_imag_conj(3 + 4j)

print(r)
