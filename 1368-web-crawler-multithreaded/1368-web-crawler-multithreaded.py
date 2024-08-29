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

        cur_queue, domain, visited = queue.Queue(), startUrl.split("http://")[1].split("/")[0], set([startUrl])
        cur_queue.put(startUrl)
        with ThreadPoolExecutor(max_workers=5) as executor:
            while not cur_queue.empty():
                futures = []
                while not cur_queue.empty():
                    futures.append(executor.submit(_crawl, cur_queue.get()))

                for future in futures:
                    result = future.result()
                    for url in result:
                        cur_queue.put(url)
        return list(visited)
                    

        