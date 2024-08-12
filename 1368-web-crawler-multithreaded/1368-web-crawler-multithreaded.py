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
from typing import List

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def _crawl(url):
            tmp = []
            for newUrl in htmlParser.getUrls(url):
                if newUrl.split("http://")[1].split("/")[0] == domain and newUrl not in visited:
                    tmp.append(newUrl)
                    visited.add(newUrl)
            return tmp

        curQueue = queue.Queue()
        visited = set([startUrl])
        domain = startUrl.split("http://")[1].split("/")[0]
        curQueue.put(startUrl)

        with ThreadPoolExecutor(max_workers=5) as executor:
            while not curQueue.empty():
                futures = []
                while not curQueue.empty():
                    url = curQueue.get()
                    futures.append(executor.submit(_crawl, url))
                
                for future in futures:
                    result = future.result()
                    for newUrl in result:
                        curQueue.put(newUrl)

        return list(visited)
