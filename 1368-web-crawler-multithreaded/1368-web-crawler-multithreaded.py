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
import threading
import queue
from concurrent.futures import ThreadPoolExecutor

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def _crawl(url):
            next_queue = []
            for new_url in htmlParser.getUrls(url):
                if new_url.split("http://")[1].split("/")[0] == domain and new_url not in visited:
                    next_queue.append(new_url)
                    visited.add(new_url)
            return next_queue

        curQueue, visited, domain = queue.Queue(), set([startUrl]), startUrl.split("http://")[1].split("/")[0]
        curQueue.put(startUrl)
        with ThreadPoolExecutor(max_workers=5) as executor:
            while not curQueue.empty():
                futures = []
                while not curQueue.empty():
                    url = curQueue.get()
                    futures.append(executor.submit(_crawl, url))
                for future in futures:
                    result = future.result()
                    for url in result:
                        curQueue.put(url)
        return list(visited)



