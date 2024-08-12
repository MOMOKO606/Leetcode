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
            tmp = []
            for new_url in htmlParser.getUrls(url):
                if new_url.split("http://")[1].split("/")[0] == domain and new_url not in visited:
                    tmp.append(new_url)
                    visited.add(new_url)
            return tmp
        
        cur_queue = queue.Queue()
        visited = set([startUrl])
        domain = startUrl.split("http://")[1].split("/")[0]
        cur_queue.put(startUrl)

        with ThreadPoolExecutor(max_workers=5) as executor:
            while not cur_queue.empty():
                futures = []
                while not cur_queue.empty():
                    url = cur_queue.get()
                    futures.append(executor.submit(_crawl, url))

                for future in futures:
                    result = future.result()
                    for new_url in result:
                        cur_queue.put(new_url)

        return list(visited)