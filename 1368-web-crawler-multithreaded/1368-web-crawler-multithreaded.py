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
import queue
from concurrent.futures import ThreadPoolExecutor

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def _crawl(url):
            nextQueue = []
            for newUrl in htmlParser.getUrls(url):
                if newUrl.split("http://")[1].split("/")[0] == domain and newUrl not in visited:
                    nextQueue.append(newUrl)
                    visited.add(newUrl)
            return nextQueue


        curQueue, domain, visited = queue.Queue(), startUrl.split("http://")[1].split("/")[0], set([startUrl])
        curQueue.put(startUrl)
        with ThreadPoolExecutor(max_workers=5) as executor:
            while not curQueue.empty():
                futures = []
                while not curQueue.empty():
                    futures.append(executor.submit(_crawl, curQueue.get()))
                for future in futures:
                    for url in future.result():
                        curQueue.put(url)
        return list(visited)        