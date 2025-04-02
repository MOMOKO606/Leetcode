class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        trans = {
            "a": 0,
            "b": 1,
            "c": 2,
            "d": 3,
            "e": 4,
            "f": 5,
            "g": 6,
            "h": 7,
            }
        return (trans[coordinate1[0]] + int(coordinate1[1])) & 1 ==  (trans[coordinate2[0]] + int(coordinate2[1])) & 1
        