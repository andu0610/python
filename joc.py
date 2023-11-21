import time, random
counter=0
player1=0
player2=0

knight1=0
swordman1=0
archer1=0
knight2=0
swordman2=0
archer2=0

hpknight=200
hpswordman=150
hparcher=100

dmgknight=20
dmgswordman=30
dmgarcher=40

knight1=int(input("PLAYER1: how many Knights ?"))
swordman1=input("PLAYER1: how many swordmen ?")
archer1=input("PLAYER1: how many archers ?")
knight2=int(input("PLAYER2: how many Knights ?"))
swordman2=input("PLAYER2: how many swordmen ?")
archer2=input("PLAYER2: how many archers ?")

hptotal_knight1=int(hpknight*knight1)
hptotal_swordman1=hpswordman*swordman1
hptotal_archer1=hparcher*archer1
hptotal_knight2=int(hpknight*knight2)
hptotal_swordman2=hpswordman*swordman2
hptotal_archer2=hparcher*archer2

dmgtotal_knight1=dmgknight*knight1
dmgtotal_swordman1=dmgswordman*swordman1
dmgtotal_archer1=dmgarcher*archer1
dmgtotal_knight2=dmgknight*knight2
dmgtotal_swordman2=dmgswordman*swordman2
dmgtotal_archer2=dmgarcher*archer2


def atack_knights(hptotal_knight2,hptotal_knight1,hpknight,dmgtotal_knight2,dmgtotal_knight1,dmgknight,knight1,knight2):
  while hptotal_knight1>0 and hptotal_knight2>0:
    hptotal_knight1=hptotal_knight1-dmgtotal_knight2
    hptotal_knight2=hptotal_knight2-dmgtotal_knight1
    dmgtotal_knight1=dmgtotal_knight1-(hptotal_knight1/hpknight)*dmgknight
    dmgtotal_knight2=dmgtotal_knight2-(hptotal_knight2/hpknight)*dmgknight
  if hptotal_knight1==0:
    knight2=hptotal_knight2/hpknight
    print("player2 has",knight2, "knights")
  if hptotal_knight2==0:
    knight1=hptotal_knight1/hpknight
    print("player1 has",knight1,"knights")
    
atack_knights(hptotal_knight2,hptotal_knight1,hpknight,dmgtotal_knight2,dmgtotal_knight1,dmgknight,knight1,knight2)

            
    
     


# while True:
    

#     while True:
#         counter+=1
#         print("The battle rages on and on ..")
#         time.sleep(.5)
#         print("...")
#         time.sleep(.5)
#         print("...")
#         time.sleep(.5)
#         print("...")

#         if counter==3:
#             break

#     print("A victor has been decided")

#     x=random.randint(1,3)

#     time.sleep(x)

#     defender1=int(defender)+random.randint(1,15)
#     farmer1=int(farmer)+random.randint(1,10)
#     knight1=int(knight)+random.randint(1,15)

    

#     if defender1>=35 and farmer1>=15 and knight1>=50:
#         player2_win()

#     else:
#         player1_win()

#     print("Orc victory:"+str(player1)+" Human victory:"+str(player2))
#     counter=0

#     if player1==5:
#         print("""The Orcs has won the war. You have been defeated !!""")
        
#         break

    
        

#     if player2==5:
#         print("The Humans has won the war, congratulations !!")
        
#         break


# input("Press enter to exit")