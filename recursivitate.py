# x=int(input())
# if x<0:
#     print("nu este posibil")
# elif x==0:
#     print(1)
# else:
#     f=1
#     for i in range(1,x+1):
#         f=f*i
#     print(f)

# def factorial(a):
#     if a==0:
#         return(1)
#     if a>0:
#         return a*factorial(a-1)
# a=int(input())
# rezultat=factorial(a)
# print(rezultat)

# def putere(a,n):
#     if a==0:
#         return 1
#     else:
#          a = a * putere(a, n-1)
#          return a
# a=int(input())
# n=int(input())
# rezultat=putere(a,n)
# print(f"rezultatul este{rezultat}")

# def suma(a,b):
#     if a>b:
#         return b+suma(a+1, b)
#     elif b>a:
#         return a+suma(a,b+1)
# a=int(input())
# b=int(input())
# rezultat=suma(a,b)
# print(rezultat)    

# b=len(list1)
def suma_vector(a,b):
        if b!=0:
            return a[b-1]+suma_vector(a,b-1)  
a=[1,2,3,4,5]

rezultat=suma_vector(a,5)
print(rezultat)