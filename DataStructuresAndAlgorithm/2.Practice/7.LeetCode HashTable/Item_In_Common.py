def Item_In_Common(list1, list2):
    my_dict ={}

    for i in list1:
        my_dict[i] = True
    for j in list2:
        if j in my_dict:
            return True
    return False

list1 =[1,2,3]
list2 =[3,2,1]

print(Item_In_Common(list1,list2))