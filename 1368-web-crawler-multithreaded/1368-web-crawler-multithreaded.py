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
            next_node = []
            for new_url in htmlParser.getUrls(url):
                if new_url.split("http://")[1].split("/")[0] == domain and new_url not in visited:
                    visited.add(new_url)
                    next_node.append(new_url)
            return next_node

        domain, visited = startUrl.split("http://")[1].split("/")[0], set([startUrl])
        cur_queue = Queue()
        cur_queue.put(startUrl)
        with ThreadPoolExecutor(max_workers=5) as executor:
            while not cur_queue.empty():
                futures = []
                while not cur_queue.empty():
                    futures.append(executor.submit(_crawl, cur_queue.get()))
                for future in futures:
                    for url in future.result():
                        cur_queue.put(url)
        return list(visited)

        