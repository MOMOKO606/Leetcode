class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        if endGene not in bank: return -1
        queue, steps = [startGene], 0
        while queue:
            next_queue = []
            for word in queue:
                if word == endGene: return steps
                for i in range(len(word)):
                    for char in "ACGT":
                        newWord = word[:i] + char + word[i + 1:]
                        if newWord in bank:
                            bank.remove(newWord)
                            next_queue.append(newWord)
            steps, queue = steps + 1, next_queue
        return -1
                        


        