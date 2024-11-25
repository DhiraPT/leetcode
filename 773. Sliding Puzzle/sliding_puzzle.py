class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = '123450'
        neighbours = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]
        start = ''.join(str(num) for row in board for num in row)

        queue = deque([(start, 0)])
        visited = set()
        visited.add(start)

        while queue:
            state, moves = queue.popleft()
            if state == target:
                return moves
            zero_index = state.index('0')

            for neighbour in neighbours[zero_index]:
                new_state = list(state)
                new_state[zero_index], new_state[neighbour] = new_state[neighbour], new_state[zero_index]
                new_state_str = ''.join(new_state)
                if new_state_str not in visited:
                    visited.add(new_state_str)
                    queue.append((new_state_str, moves + 1))

        return -1