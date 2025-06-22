def demodula_nrz_polar(mensagem):
    dem_nrz_p = []

    for mod in mensagem:
        if (mod == 1):
            dem_nrz_p.append(1)
        else:
            dem_nrz_p.append(0)

    return dem_nrz_p

def demodula_machester(mensagem):
    dem_manch = []
    um = [-1, 1]

    for i in range(0,len(mensagem),2):
        print(mensagem[i:i+2])
        if mensagem[i:i+2] == um:
            dem_manch.append(1)
        else:
            dem_manch.append(0)

    return dem_manch

def demodula_bipolar(mensagem):
    dem_bip = []

    for mod in mensagem:
        if (mod == 1 or mod == -1):
            dem_bip.append(1)
        else:
            dem_bip.append(0)
    
    return dem_bip
