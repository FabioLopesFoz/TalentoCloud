pisoInicial = 0
pisoFinal = 20

for i in range(pisoInicial, pisoFinal+1):
    if(i == 0 ):
        print("Piso Terreo")
    elif((i >= 0) and (i != 13)):
        print("Piso: %s" %(i))
