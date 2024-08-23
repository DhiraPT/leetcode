class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        step = 1
        direction = (0, 1)
        pos = [rStart, cStart]
        visited = [[rStart, cStart]]

        while len(visited) < rows * cols:
            for _ in range(2):
                for _ in range(step):
                    pos[0] += direction[0]
                    pos[1] += direction[1]
                    if 0 <= pos[0] < rows and 0 <= pos[1] < cols:
                        visited.append([pos[0], pos[1]])
                direction = (direction[1], -direction[0])
            step += 1

        return visited