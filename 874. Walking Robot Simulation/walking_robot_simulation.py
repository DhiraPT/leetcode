class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = set(map(tuple, obstacles))

        direction = (0, 1)
        pos = [0, 0]
        max_distance_squared = 0

        for c in commands:
            if c == -2:
                direction = (-direction[1], direction[0])
            elif c == -1:
                direction = (direction[1], -direction[0])
            else:
                while c > 0:
                    if (pos[0] + direction[0], pos[1] + direction[1]) in obstacles:
                        break
                    pos[0] += direction[0]
                    pos[1] += direction[1]
                    c -= 1
                max_distance_squared = max(max_distance_squared, pos[0]**2 + pos[1]**2)

        return max_distance_squared