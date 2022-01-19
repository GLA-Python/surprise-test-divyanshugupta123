def expanding(lst):
    
    c=True
    for j in range(1,len(lst)-1):
        a=abs(lst[j]-lst[j-1])
        b=abs(lst[j+1]-lst[j])
        if a<b:
            c=True
        else:
            c= False
    return c
a=input('enter the element ').split()
lst=list(map(int,a))
print(expanding(lst))