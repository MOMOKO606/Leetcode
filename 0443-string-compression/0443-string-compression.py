class Solution:
    def compress(self, chars: List[str]) -> int:
        i, cur, count = -1, chars[0], 1
        for j in range(1, len(chars) + 1):
            if j < len(chars) and chars[j] == chars[j - 1]: 
                count += 1
            else:
                i += 1
                chars[i] = cur
                if count > 1: 
                    count = list(str(count))
                    chars[i + 1: i + 1 + len(count)] = count
                    i = i + len(count)
                if j < len(chars): cur, count = chars[j], 1
        return i + 1

        