
def solution(A):
    east_cars = 0  # Count of cars traveling east
    passing_count = 0  # Count of passing pairs

    for car in A:
        if car == 0:  # Car traveling east
            east_cars += 1
        else:  # Car traveling west
            passing_count += east_cars
            if passing_count > 1000000000:
                return -1

    return passing_count

print(solution([0,0,1,1]))
