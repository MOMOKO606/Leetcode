class Solution:
    # DFS
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfsHelper(i = 0):
            if i in visited: return 
            visited.add(i)
            for neighbour in rooms[i]:
                dfsHelper(neighbour)
        
        visited = set()
        dfsHelper()
        return len(rooms) == len(visited)


        