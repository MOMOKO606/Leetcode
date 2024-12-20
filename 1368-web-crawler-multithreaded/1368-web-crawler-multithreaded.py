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
from queue import Queue
from threading import Thread

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def _crawl():
            while True:
                tmp = []
                for url in htmlParser.getUrls(cur_queue.get()):
                    if url not in visited and url.split("http://")[1].split("/")[0] == domain:
                        tmp.append(url)
                        visited.add(url)
                next_queue.put(tmp)


        domain = startUrl.split("http://")[1].split("/")[0]
        cur_queue, next_queue, visited, running = Queue(), Queue(), set([startUrl]), 1
        cur_queue.put(startUrl)
        for _ in range(5):
            thread = Thread(target=_crawl, daemon=True)
            thread.start()
        
        while running:
            for url in next_queue.get():
                cur_queue.put(url)
                running += 1
            running -= 1
        return list(visited)


        