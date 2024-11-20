class Solution:
    def compress(self, chars: List[str]) -> int:
        def update(i, char, count):
            chars[i], i = char, i + 1
            if count > 1:
                target = []
                while count:
                    target.append(str(count % 10))
                    count //= 10
                chars[i: i + len(target)] = target[::-1]
                i += len(target)
            return i


        count, i = 1, 0
        for j in range(1, len(chars) + 1):
            if j == len(chars) or chars[j] != chars[j - 1]:
                i = update(i, chars[j - 1], count)
                count = 1
            else:
                count += 1
        return i

        