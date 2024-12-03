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
from threading import Thread
from queue import Queue

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def _crawl():
            tmp = []
            while True:
                for url in htmlParser.getUrls(curQueue.get()):
                    if url.split("http://")[1].split("/")[0] == domain and url not in visited:
                        visited.add(url)
                        tmp.append(url)
                nextQueue.put(tmp)


        curQueue, nextQueue, running, visited = Queue(), Queue(), 1, set([startUrl])
        domain = startUrl.split("http://")[1].split("/")[0]
        curQueue.put(startUrl)
        for _ in range(5):
            thread = Thread(target=_crawl, daemon=True)
            thread.start()
        
        while running:
            for url in nextQueue.get():
                curQueue.put(url)
                running += 1
            running -= 1
        return list(visited)
        