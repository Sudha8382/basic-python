# # # # # # l=[20,30,50,60]
# # # # # # '''l.pop(2)
# # # # # # print(l)
# # # # # # print(l.pop(2))
# # # # # # l.clear()'''
# # # # # # l.insert(1,80)
# # # # # # print(l)

# # # # # l=[10,20,30,40,50,60]
# # # # # n=[90,80,90]
# # # # # l.extend(n)
# # # # # print(l)

# # # l=[10,30,20,10,60,20,10]
# # # # m=max(l)
# # # # print(m)
# # # # a=l.count(10)
# # # # print(a)

# # # n=['hello','world']
# # # print(min(n))

# # # l.sort()
# # # print(l)

# # l=[10,20,30,40]
# # l1=[2,4,7,9,1]
# # t=len(l)
# # for a,b in zip(l,l1):
# #     print(a,b)

# # for h in range(t):
# #     print(l[h],l1[h])


# n=input("enter the value")
# l=n.split()
# print(l)

l=[]
for a in range (1,4):
    n=input("enter the value"+str(a)+"red:")
    l.append(n)
print(l)
