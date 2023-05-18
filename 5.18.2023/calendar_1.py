class Data:
    def __init__(self, zi, luna, an):
        self.zi=zi
        self.luna= luna
        self.an= an
    
    def __str__(self):
        return(f"{self.zi}, {self.luna}, {self.an}")
    
    def zi_urm(self):
        if self.luna==1 or self.luna==3 or self.luna==5 or self.luna==7 or self.luna==8 or self.luna==10 or self.luna==12:
            
            if self.luna==12 and self.zi==31:
                self.luna==1
                self.zi==1
                self.an=self.an-1
            if self.zi==31:
                self.luna=self.luna+1
                self.zi=1
            if self.zi>31:
                print('nu exista')
            else:
                print(self.zi, self.luna, self.an)
        
        if self.luna==4 or self.luna==6 or self.luna==9 or self.luna==11:
        
            if self.zi==30:
                self.luna=self.luna+1
                self.zi=1
            if self.zi>30:
                print('nu exista')
            else:
                print(self.zi, self.luna, self.an)
        if self.luna==2:
            if self.zi==29 and self.an%4==0:
                self.zi=1
                self.luna=3
                if self.zi>29:
                    print('nu exista')
                else:
                    print(self.zi, self.luna, self.an)
            if self.zi==28 and self.an%4==0:
                self.zi=29
                if self.zi>28:
                    print('nu exista')
                else:
                    print(self.zi, self.luna, self.an)

            if self.zi==28 and self.an%4!=0:
                self.zi=1
                self.luna=3
                if self.zi>28:
                    print('nu exista')
                else:
                    print(self.zi, self.luna, self.an)
        
        print(self.zi, self.luna, self.an)

data1= Data( 29, 2, 2001)  
print(data1)             
data1.zi_urm()          
        
            