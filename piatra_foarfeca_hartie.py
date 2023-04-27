import random
optiune_pc=None
optiune_jucator=None
optiuni=('piatra','foarfeca','hartie')
rulare_joc = True
print('poti juca pana mai castigi')

def verificare(optiune1,optiune2):
    
    if optiune1==optiune2:
        print('egalitate')
    elif optiune1=='piatra'and optiune2=="foarfeca":
        print('ai pierdut')
    elif optiune1=="foarfeca" and optiune2=="hartie":
        print('ai pierdut')
    elif optiune1=='hartie' and optiune2=="piatra":
        print('ai pierdut')
    else:
        print('ai castigat')
        return False

while rulare_joc==True:
    optiune_pc=random.choice(optiuni)
    optiune_jucator= input('alege piatra, foarfeca sau hartie ')
    
    # if optiune_jucator!='hartie':
    #     print('alege altceva')
    #     optiune_jucator= input('alege piatra, foarfeca sau hartie ')
    # elif optiune_jucator!='piatra':
    #     print('alege altceva')
    #     optiune_jucator= input('alege piatra, foarfeca sau hartie ')
    # elif optiune_jucator!= 'foarfeca':
    #     print('alege altceva')
    #     optiune_jucator= input('alege piatra, foarfeca sau hartie ')
    while optiune_jucator not in optiuni:
        print('alege altceva')
        optiune_jucator= input('alege piatra, foarfeca sau hartie ')
    print('ai ales ' + optiune_jucator)
    print('am ales ' + optiune_pc)
    
    rulare_joc=verificare(optiune_pc,optiune_jucator)
    
        

    
    # if optiune_pc==optiune_jucator:
    #     print('egalitate')
    # elif optiune_pc=='piatra'and optiune_jucator=="foarfeca":
    #     print('ai pierdut')
    # elif optiune_pc=="foarfeca" and optiune_jucator=="hartie":
    #     print('ai pierdut')
    # elif optiune_pc=='hartie' and optiune_jucator=="piatra":
    #     print('ai pierdut')
    # else:
    #     print('ai castigat')
    #     rulare_joc=False
    

