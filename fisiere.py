
#'r'=read
#'w'=write
#'a'=append
#'x'=new_file

# print(fisier.read(5))
# print(fisier.read(2))
# fisier.seek(0)
# print(fisier.read(3))

# fisier.readline()
# print(fisier.readline())

# print(fisier.readlines())

# for linie in fisier.readlines():
#     if linie.startswith("1"):
#         print(line)
# fisier = open("fisierul_meu2.txt","w")
# fisier.write('merec')
# fisier.write("aaaaaaaaa")
# fisier.close
# fisier=open("fisierul_meu2.txt")
# print(fisier.read(50))

# fisier=open("fisierul_meu2.txt","w")
# fisier.write('asgjvdagjxc')
# fisier.close
# fisier=open("fisierul_meu2.txt","r")
# print(fisier.readlines())
# fisier=open("fisierul_meu.txt","a")
# fisier.write("aaaaaaaa")
# fisier.close
# f=open("altfisier.txt","x")
# f.close
# f = open("altfisier.txt","x")
# f.close
import os
#  os.remove("altfisier.txt")
if os.path.exists("fisierul_meu.txt"):
    os.remove("fisierul_meu.txt")
else:
   print("nu avem")