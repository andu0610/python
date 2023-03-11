# def printare():
#     print('aaaaa')
#     print('bbbbb')
# printare()

# def suma(a,b,c):
#     suma=a+b+c
#     print(suma)
# suma(10,20,30)


# def suma_3nr(a,b,c):
#     suma=a+b+c
#     return suma

# rezultat= 2+suma_3nr(2,4,6)
# print(rezultat)

# def suma_3nr(a,b,c):
#     suma=a+b+c
#     return suma
# rezultat=suma_3nr(b=10,a=20,c=70) 
# print(rezultat)

# def putere(a,b):
#     n=a
#     for i in range(1,b):
#         a=n*a   
#     return a


# rez=putere(2,5)
# print (rez)

def paritate(a):
    if(a%2==0):
        print(a)
        return a

a=int(input("introdu nr"))
b=int(input('introdu nr'))
for i in range(a,b):
    paritate(i)
