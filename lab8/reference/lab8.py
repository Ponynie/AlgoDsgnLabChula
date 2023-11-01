def divide(alist):
    if len(alist)>1:

        even = [alist[x] for x in range(len(alist)) if x % 2 == 0]
        odd = [alist[x] for x in range(len(alist)) if x % 2 != 0]

        divide(even)
        divide(odd)

    else:
        blist.append(alist[0])

a = int(input("Enter n:"))
blist = []
alist = list(range(a+1))
divide(alist)
print(blist)