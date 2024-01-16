pisoInicial = 0
pisoFinal = 20

while pisoFinal >=  pisoInicial:
    if(pisoFinal == 0 ):
        print("Piso Terreo")
    elif((pisoFinal >= 0) and (pisoFinal != 13)):
        print("Piso: %s" %(pisoFinal))
    pisoFinal = pisoFinal-1