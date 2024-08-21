class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0

        def isMagicSquare(row, col):
            found = [False] * 10
            for i in range(3):
                for j in range(3):
                    num = grid[row+i][col+j]
                    if num < 1 or num > 9:
                        return False
                    if found[num]:
                        return False
                    found[num] = True

            diagonal1_sum = grid[row][col] + grid[row+1][col+1] + grid[row+2][col+2]

            if diagonal1_sum != grid[row+2][col] + grid[row+1][col+1] + grid[row][col+2]:
                return False

            for i in range(3):
                if grid[row+i][col] + grid[row+i][col+1] + grid[row+i][col+2] != diagonal1_sum:
                    return False
                if grid[row][col+i] + grid[row+1][col+i] + grid[row+2][col+i] != diagonal1_sum:
                    return False

            return True

        for row in range(m-2):
            for col in range(n-2):
                if isMagicSquare(row, col):
                    count += 1

        return count