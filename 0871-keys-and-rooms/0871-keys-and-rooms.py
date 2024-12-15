class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # Build the graph
        graph = collections.defaultdict(list)
        for i, room in enumerate(rooms):
            graph[i] = room

        queue, visited = [0], set([0])
        while queue:
            next_queue = []
            for node in queue:
                for neighbor in graph[node]:
                    if neighbor in visited: continue
                    visited.add(neighbor)
                    next_queue.append(neighbor)
            queue = next_queue
        return len(visited) == len(rooms)
        