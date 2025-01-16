class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visited = collections.defaultdict(int)
        for cpdomain in cpdomains:
            cpdomain = cpdomain.split()
            count, domain = int(cpdomain[0]), cpdomain[1]
            domains, j = domain.split("."), 0
            for i in range(len(domains)):
                visited[domain[j:]] += count
                j += len(domains[i]) + 1
        return [str(count) + " " + domain for domain, count in visited.items()]
        