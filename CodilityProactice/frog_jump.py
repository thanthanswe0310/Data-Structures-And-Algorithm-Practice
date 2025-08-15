def Solution(X,Y,D):
    distance_to_cover =Y-X
    Jump_needed = distance_to_cover//D

    if distance_to_cover%D !=0:
        Jump_needed+=1
    return Jump_needed



# print(Solution(2,6,23))


# def Solution(X,Y,D):
#     v = (Y-X)//D
#     print(X+v*D)
#     if X+v*D >=Y:
#         return v
#     else: 
#         return v+1
#     pass 

print(Solution(1,30,10))