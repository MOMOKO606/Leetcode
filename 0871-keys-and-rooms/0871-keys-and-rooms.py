class Solution:
    # BFS
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        deque, visited = collections.deque([0]), set([0])
        while deque:
            node = deque.popleft()
            for neighbour in rooms[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    deque.append(neighbour)
        return len(rooms) == len(visited)
        