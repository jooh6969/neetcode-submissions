class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check each row for duplicates
        for row in range(9):
            seen = {}
            for col in range(9):
                char = board[row][col]
                if char in seen and char != "." :
                    return False
                seen[char] = seen.get(char, 0) + 1
        # check each col for duplicates
        for col in range(9):
            seen = {}
            for row in range(9):
                char = board[row][col]
                if char in seen and char != ".":
                    return False
                seen[char] = seen.get(char, 0) + 1
        # 0 1 2 -> 0
        # 3 4 5 -> 1
        # 6 7 8 -> 2
        # we take row and col // 3 to get the index
        seen = [[{} for _ in range(3)] for _ in range(3)]
        for row in range(9):
            for col in range(9):
                row_idx = row // 3
                col_idx = col // 3
                char = board[row][col]
                curr_dict = seen[row_idx][col_idx]
                if char in curr_dict and char != ".":
                    return False
                curr_dict[char] = curr_dict.get(char, 0) + 1
        return True

                
