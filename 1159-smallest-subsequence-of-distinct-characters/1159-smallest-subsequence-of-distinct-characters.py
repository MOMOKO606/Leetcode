class Solution:
    def smallestSubsequence(self, s: str) -> str:
        boundries, stack, inserted = {}, [], set()
        for i, char in enumerate(s):
            boundries[char] = i

        for i, char in enumerate(s):
            if char in inserted: continue
            while stack and char < stack[-1] and i < boundries[stack[-1]]:
                node = stack.pop()
                inserted.remove(node)
            stack.append(char)
            inserted.add(char)
        return "".join(stack)
