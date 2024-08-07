def solution(grid):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    subgrids = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            if grid[r][c] == '.':
                continue
            num = grid[r][c]
            subgrid_idx = (r // 3) * 3 + (c // 3)
            
            if num in rows[r]:
                return False
            if num in cols[c]:
                return False
            if num in subgrids[subgrid_idx]:
                return False

            rows[r].add(num)
            cols[c].add(num)
            subgrids[subgrid_idx].add(num)
    
    return True

# 예제 입력 테스트
grid1 = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
         ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
         ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
         ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
         ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
         ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
         ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
print(solution(grid1))  # True

grid2 = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
         ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
         ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
         ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
         ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
         ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
         ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
         ['.', '2', '.', '.', '3', '.', '.', '.', '.']]
print(solution(grid2))  # False


grid3 = [[".","4",".",".",".",".",".",".","."], 
        [".",".","4",".",".",".",".",".","."], 
        [".",".",".","1",".",".","7",".","."], 
        [".",".",".",".",".",".",".",".","."], 
        [".",".",".","3",".",".",".","6","."], 
        [".",".",".",".",".","6",".","9","."], 
        [".",".",".",".","1",".",".",".","."], 
        [".",".",".",".",".",".","2",".","."], 
        [".",".",".","8",".",".",".",".","."]]

print(solution(grid3))  # False