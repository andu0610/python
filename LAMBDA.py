# v1=lambda x,y,z: x+y+z
# print(type(v1))
# print(v1(1,2,3))

# def concat(list1):
#     list2=[]
#     for i in range(10):
#         for j in range(5):
#             list2.append(i*j)
#     return list1+list2
# print(concat(['1','2','3']))  

x=lambda list1: [i+j for i in range(5) for j in range(5)]+list1
print(type(x))
lista_finala=x(['incepem', 'lista: '])
print(lista_finala)