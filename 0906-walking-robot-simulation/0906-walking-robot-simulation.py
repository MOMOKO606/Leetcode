class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = {
            "N": ("W", "E", [0, 1]), 
            "S": ("E", "W", [0, -1]), 
            "W": ("S", "N", [-1, 0]),
            "E": ("N", "S", [1, 0]),
            }
        cur_dir, i, j, ans, obstacles = "N", 0, 0, 0, set(map(tuple, obstacles))
        for command in commands:
            if command == -2:
                cur_dir = directions[cur_dir][0]
            elif command == -1:
                cur_dir = directions[cur_dir][1]
            else:
                di, dj = directions[cur_dir][2]
                while command and (i + di, j + dj) not in obstacles:
                    i, j, command = i + di, j + dj, command - 1
            ans = max(ans, i * i + j * j)
        return ans

        