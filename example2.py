#input del usuario
pesocol = input("¿Cuántos pesos colombianos tienes?")
pesocol = float(pesocol)

#declaracion de valores
valor_dolar = 3679
valor_euro = 4383
valor_cake = 58800
valor_btc = 136134100

#calculo valor dolar
dolares =  pesocol / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)

#calculo valor euro
euros = pesocol / valor_euro
euros = round(euros, 2)
euros = str(euros)

#calculo cantidad de cake
cakes = pesocol / valor_cake
cakes = round(cakes, 4)
cakes = str(cakes)

#calculo bitcoin
btcs = pesocol / valor_btc
btcs = round(btcs, 9)
btcs = str(btcs)

#prints
print("Tienes $" + dolares + " dolares")
print("Tienes €" + euros + " euros")
print("Tienes: " + cakes + " cakes")
print("Tienes: " + btcs + " bitcoins")
