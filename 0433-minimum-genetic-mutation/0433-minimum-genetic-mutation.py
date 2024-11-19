class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        if endGene not in bank: return -1
        queue, steps = [startGene], 0
        while queue:
            nextQueue = []
            for gene in queue:
                if gene == endGene: return steps
                for i in range(len(gene)):
                    for char in "ACGT":
                        newGene = gene[:i] + char + gene[i + 1:]
                        if newGene in bank:
                            nextQueue.append(newGene)
                            bank.remove(newGene)
            queue, steps = nextQueue, steps + 1
        return -1



        