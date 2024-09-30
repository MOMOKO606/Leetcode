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
import queue, threading

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def _crawl():
            while True:
                tmp = []
                for url in htmlParser.getUrls(curQueue.get()):
                    if url.split("http://")[1].split("/")[0] == domain and url not in visited:
                        visited.add(url)
                        tmp.append(url)
                nextQueue.put(tmp)

        curQueue, nextQueue, visited, domain, running = queue.Queue(), queue.Queue(), set([startUrl]), startUrl.split("http://")[1].split("/")[0], 1
        curQueue.put(startUrl)
        for _ in range(5):
            thread = threading.Thread(target=_crawl, daemon=True)
            thread.start()

        while running:
            for url in nextQueue.get():
                curQueue.put(url)
                running += 1
            running -= 1
        return list(visited)
        