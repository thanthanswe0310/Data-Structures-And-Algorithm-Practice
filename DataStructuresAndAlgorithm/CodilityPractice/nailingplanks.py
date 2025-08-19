def solution(A, B, C):
    def find_min_nails(A, B, C):
        sorted_nails = sorted(C)
        nails_used = 0
        current_nail_idx = 0

        for i in range(len(A)):
            plank_start = A[i]
            plank_end = B[i]

            # Find the first nail that can be used to nail the current plank
            while current_nail_idx < len(sorted_nails):
                nail_position = sorted_nails[current_nail_idx]
                if nail_position >= plank_start and nail_position <= plank_end:
                    # Nail found within the plank's range
                    nails_used += 1
                    break
                current_nail_idx += 1

            # If no nail found within the plank's range, return -1
            if current_nail_idx >= len(sorted_nails):
                return -1

        return nails_used

    return find_min_nails(A, B, C)

