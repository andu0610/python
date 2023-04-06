# list1=[]
# for i in range(10):
#     r=i*i
#     list1.append(r)
# print(list1)

# list2=[j**2 for j in range(10)]
# print(list2)

# list3=[k for k in range(10) if k>5 ]
# print(list3)

# set1={x for x in range(10) if x>5}
# print(set1)
# print(type(set1))

# dictionar1={i:i*i for i in range(10) if i>5}
# print(dictionar1)
# print(type(dictionar1))

tuple1=tuple(x**2 for x in range(10))
print(tuple1)