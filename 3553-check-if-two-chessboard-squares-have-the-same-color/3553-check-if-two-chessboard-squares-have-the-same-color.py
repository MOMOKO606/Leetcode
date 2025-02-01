class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        transfer = {
            "a": 1,
            "b": 2,
            "c": 3,
            "d": 4,
            "e": 5,
            "f": 6,
            "g": 7,
            "h": 8
            }

        return (transfer[coordinate1[0]] + int(coordinate1[1])) & 1 == (transfer[coordinate2[0]] + int(coordinate2[1])) & 1
        
        