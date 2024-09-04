class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        visited[0] = True
        num_visited = 1
        stack = [0]

        while stack:
            i = stack.pop()
            for key in rooms[i]:
                if not visited[key]:
                    visited[key] = True
                    num_visited += 1
                    stack.append(key)
                    if num_visited == len(rooms):
                        return True

        return num_visited == len(rooms)