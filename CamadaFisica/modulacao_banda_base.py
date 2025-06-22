# Modulação  NRZ-Polar
def nrz_polar(bits):
    #v = 2
    nrz_p = []
    for bit in bits:
        #amp = v / 2
        if bit == '1':
            nrz_p.append(1)
        else:
            nrz_p.append(-1)
    
    return nrz_p

# Modulação  Manchester            
def manchester(bits):
    #v = 2
    manch = []
    
    for bit in bits:
        #amp = v / 2
        if bit == '1':
            manch.append(-1)
            manch.append(1)
        else:
            manch.append(1)
            manch.append(-1)
          
    return manch

# Modulação  Bipolar
def bipolar(bits):
    v = 1
    bipo = []
    sinal = False
    
    
    for bit in bits:
        #Verifica se o bit anterior era = 1
        if bit == '1' and sinal:
            bipo.append(-v)
            sinal = False
        
        #Verifica se o bit anterior era != 1
        elif bit == '1' and not sinal:
            bipo.append(v)
            sinal = True
        
        #Se o bit anterior for 0, continua 0
        else:
            bipo.append(0)
    
    return bipo


#grafico_digital("1010011")
#print(bipolar("1010011"))
