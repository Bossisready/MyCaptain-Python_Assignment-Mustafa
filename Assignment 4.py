def list1():
    print("List 1: ")
    list=[12,-7,5,64,-14]
    k=len(list)
    for i in range(0,k):
        if list[i]>0:
            print(list[i])
        else:
            continue

def list2():
    print("List 2: ")
    list=[12,14,-95,3]
    k=len(list)
    for i in range(0,k):
        if list[i]>0:
            print(list[i])
        else:
            continue
        

list1()
list2()