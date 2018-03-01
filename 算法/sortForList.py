lst=[2, 4, 6, 4, 2, 3, 8, 5]
# sorted => newlist
# x>y为降序排列；x<y为升序排列

def sort(list):
    newlist=[]
    for x in lst:
        for i,y in enumerate(newlist):
            if x > y:
                newlist.insert(i,x)
                break
        else:
            newlist.append(x)
    return newlist

print (sort(lst))