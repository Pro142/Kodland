import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
otra_variable = int(input ('Cantidad de caracteres para tu contrseña'))
vacia = ''
for i in range(otra_variable):
    vacia += (random.choice(caracteres))
print (vacia)