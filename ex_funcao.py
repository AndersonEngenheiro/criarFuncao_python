# lista = 2, 4

# p = (len(lista))

# print(p)


from traceback import print_tb


def calculaMedia(notas):
    resultado = sum(notas) / len(notas)
    return resultado

# print(calculaMedia([2,6,7,9]))

def bonus(media, n):
    resultado = (media * (1 +(n/100)))
    return resultado

m = calculaMedia([2,6,7,9])

# print(m)
# print(bonus(m,10))

print(bonus(calculaMedia([2,6,7,9]),10))