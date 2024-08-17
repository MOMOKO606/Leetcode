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

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def _crawl():
            while True:
                tmp = []
                for new_url in htmlParser.getUrls(curQueue.get()):
                    if new_url.split("http://")[1].split("/")[0] == domain and new_url not in visited:
                        tmp.append(new_url)
                        visited.add(new_url)
                nextQueue.put(tmp)

        

        curQueue, nextQueue, running, domain, visited = queue.Queue(), queue.Queue(), 1, startUrl.split("http://")[1].split("/")[0], set([startUrl])
        curQueue.put(startUrl)

        for _ in range(5):
            thread = threading.Thread(target=_crawl, daemon=True)
            thread.start()

        while running:
            for url in nextQueue.get():
                curQueue.put(url)
                running += 1
            running -= 1
        return list(visited)
        