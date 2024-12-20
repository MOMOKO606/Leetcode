# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        domain, visited, queue = startUrl.split("http://")[1].split("/")[0], set([startUrl]), [startUrl]
        while queue:
            next_queue = []
            for url in queue:
                for neighbor in htmlParser.getUrls(url):
                    if neighbor not in visited and neighbor.split("http://")[1].split("/")[0] == domain:
                        visited.add(neighbor)
                        next_queue.append(neighbor)
            queue = next_queue
        return list(visited)
        