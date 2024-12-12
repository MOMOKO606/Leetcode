class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def get_atom(j):
            atom, j = formula[j], j + 1
            while j < len(formula) and formula[j].islower():
                atom, j = atom + formula[j], j + 1
            return atom, j - 1

        def get_count(j):
            count = 0
            while j < len(formula) and formula[j].isdigit():
                count, j = count * 10 + int(formula[j]), j + 1
            if count: return count, j - 1
            else: return 1, j - 1
            

        stack, j, ans = [{}], 0, ""
        while j < len(formula):
            if formula[j] == ")":
                count, j = get_count(j + 1)
                node = stack.pop()
                for atom, freq in node.items():
                    stack[-1][atom] = stack[-1].get(atom, 0) + count * freq
            elif formula[j] == "(":
                stack.append({})
            else:
                atom, j = get_atom(j)
                count, j = get_count(j + 1)
                stack[-1][atom] = stack[-1].get(atom, 0) + count 
            j += 1
        
        for atom, freq in sorted(stack[-1].items()):
            ans += atom + str(freq) if freq > 1 else atom
        return ans


        