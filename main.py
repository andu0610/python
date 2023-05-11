###CLASE/OBIECTE###
# class Masina:
#     an = 0
#     marca = ""
# masinamea=Masina()
# masinamea.an=2000
# masinamea.marca='BMW'
# print('am o masina'+ masinamea.marca+'din', masinamea.an)

# class Persoana:
#     varsta=10
#     def getvarsta(self):
#         print(self.varsta)
#     nume=""
    
# pers1=Persoana()
# pers1.getvarsta()


# class Dreptunghi:
#     lungime=0
#     latime=0
#     def arieprint(self):
#         print(self.lungime*self.latime)
#     # def ariereturn(self):
#     #     return(self.lungime*self.latime)
# tablou=Dreptunghi()
# tablou.latime=10
# tablou.lungime=20
# tablou.arieprint()
# # print(tablou.ariereturn)

###CONSTRUCTORI###
# class Dreptunghi:
#     def __init__(self,lungime,latime):
#         self.lungime=lungime
#         self.latime=latime
#     def arieprint(self):
#         print(self.lungime*self.latime)
    
# tablou=Dreptunghi(10,5)
# tablou.arieprint()

class Persoana:
    def __init__(self,nume,prenume,varsta):
        self.nume=nume
        self.prenume=prenume
        self.varsta=varsta
    def npvprint(self):
        print(self.nume)
        print(self.prenume)
        print(self.varsta)
    def persmajora(self):
        if(self.varsta>=18):
            print('persoana este majora')
        else:
            print('persoana este minora')
pers=Persoana('Aaaa','Bbbb',18)
pers.npvprint()
pers.persmajora()

