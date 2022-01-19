def expanding(lst):
    a=abs(lst[1]-lst[0])
    for j in range(2,len(lst)):
        b=abs(lst[j]-lst[j-1])
        if a<b:
            return True
        else:
            return False
a=input('enter the element ').split()
lst=list(map(int,a))
print(expanding(lst))