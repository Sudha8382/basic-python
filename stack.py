l=[]
while True:
    c=int(input('''
    1 push elements
    2 pop elements
    3 peek elements
    4 display stack
    5 exit'''))

    if c==1:
        n=input("enter the value"):
        l.append(n)
        print(l)
    if c==2:
        p=l.pop()
        print(p)
        print(l)
        

