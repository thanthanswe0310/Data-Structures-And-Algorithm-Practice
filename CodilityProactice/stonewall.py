def solution(H):
    stack = []  # Stack to keep track of block heights
    blocks_needed = 0  # Count of blocks needed
    
    for height in H:
        # Remove blocks from the stack until the current height is greater than the top of the stack
        while stack and height < stack[-1]:
            stack.pop()
        
        # If the stack is empty or the current height is greater than the top of the stack, add a new block
        if not stack or height > stack[-1]:
            blocks_needed += 1
            stack.append(height)
    
    return blocks_needed

print(solution([2,2,3,4,5,4]))