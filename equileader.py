def solution(A):
    # Find the leader of the array using Boyer-Moore Majority Vote algorithm
    leader = None
    count = 0
    for num in A:
        if count == 0:
            leader = num
            count += 1
        elif num == leader:
            count += 1
        else:
            count -= 1

    # Check if the leader occurs more than half of the elements
    leader_count = A.count(leader)
    if leader_count <= len(A) // 2:
        return 0  # If the leader does not exist, there are no equi leaders

    equi_leader_count = 0
    leader_count_prefix = 0
    leader_count_suffix = leader_count
    for i, num in enumerate(A):
        if num == leader:
            leader_count_prefix += 1
            leader_count_suffix -= 1

        if leader_count_prefix > (i + 1) // 2 and leader_count_suffix > (len(A) - i - 1) // 2:
            equi_leader_count += 1

    return equi_leader_count

# Test case
A = [4, 3, 4, 4, 4, 2]
print(solution(A))  # Output: 2
