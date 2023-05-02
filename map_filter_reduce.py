# x=lambda a,b,c: (a+b+c)/3
# print(x(1,2,3))

###MAP###
# list1=[1,2,3,4]

# list2=[]
# for i in list1:
#     list2.append(i*10)
# print (list2)

# def ori_10(x):
#     return x*10



# list2=list(map(lambda x: x*10, list1))
# print(list2)

###FILTER###

# def maimicdecat18(x):
#     if x<18:
#         return True
    
# list1=[1,19,37,3,9,90,98,6]
# list2=list(filter(maimicdecat18,list1))
# print(list2)

# list3=[]
# for i in range (50):
#     list3.append(i)
    
# print (list3)
    
# def nrprim(x):
#     d=2
#     k=0
#     while d<=x/2:
#         if x%d==0:
#             k=1
#         d=d+1
#     if k==0 and x!=0 and x!=1:
#         return True
    
# list4=list(filter(nrprim, list3))
# print(list4)

###REDUCE###

from functools import reduce

list1=[1,2,3,4]
# S=0
# for i in list1:
#     S=S+i
# print(S)

print(reduce (lambda a,b: a+b,list1))

print(reduce (lambda a,b: a+ ' '+b , 'python') )