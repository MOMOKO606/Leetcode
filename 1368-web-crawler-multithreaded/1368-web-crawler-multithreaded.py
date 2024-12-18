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
from queue import Queue


class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def _crawl(url):
            tmp = []
            for new_url in htmlParser.getUrls(url):
                if new_url.split("http://")[1].split("/")[0] == domain and new_url not in visited:
                    tmp.append(new_url)
                    visited.add(new_url)
            return tmp


        domain, curQueue, visited = startUrl.split("http://")[1].split("/")[0], Queue(), set([startUrl])
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

            

        