import threading, queue

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def _crawl():
            while True:
                tmp = []
                for url in htmlParser.getUrls(curQueue.get()):
                    if url.split("http://")[1].split("/")[0] == domain and url not in visited:
                        tmp.append(url)
                        visited.add(url)
                nextQueue.put(tmp)
        
        
        
        curQueue, nextQueue, visited, running, domain = queue.Queue(), queue.Queue(), set([startUrl]), 1, startUrl.split("http://")[1].split("/")[0]
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
