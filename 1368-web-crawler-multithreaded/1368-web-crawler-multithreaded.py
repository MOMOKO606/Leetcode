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

from concurrent.futures import ThreadPoolExecutor
from threading import Condition

class Solution:
    def __init__(self) -> None:
        self._queue = list()
        self._lock = Condition()
        self._visited = set()

    def get_hostname(self, url: str):
        hostname = '.'.join(url.split('/')[2].split('.')[1:]) 
        return hostname

    def visit_url(self, url: str):
        next_urls: List[str] = self._parser.getUrls(url)

        with self._lock:
            for next_url in next_urls:
                if next_url not in self._visited and self.current_hostname == self.get_hostname(next_url) :
                    self._visited.add(next_url)
                    self._queue.insert(0,next_url)



    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        self._queue.insert(0,startUrl)
        self._visited.add(startUrl)
        self.current_hostname = self.get_hostname(startUrl)
        self._parser = htmlParser
        
        executor = ThreadPoolExecutor()

        while self._queue:
            urls = [self._queue.pop(), ]

            while self._queue:
                urls.append(self._queue.pop())

            excecutor_list = [executor.submit(self.visit_url, (url)) for url in urls]
            for future in excecutor_list:
                future.result()
        
        executor.shutdown()

        return list(self._visited)
        