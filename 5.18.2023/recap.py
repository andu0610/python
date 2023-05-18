class Persoana:
    # nume=''
    # varsta=0
    def __init__ (self, nume='', varsta=0):
        self.nume=nume
        self.varsta=varsta

    # def pers_print(self):
        # print(self.nume)
        # print(self.varsta)

    def __str__(self):
        return(f"{self.nume}, {self.varsta}")
    
Gigel=Persoana('sonescu', 30)
# Gigel.nume='gigel sonescu'
# Gigel.varsta=30
# Gigel.pers_print()
print(Gigel)

