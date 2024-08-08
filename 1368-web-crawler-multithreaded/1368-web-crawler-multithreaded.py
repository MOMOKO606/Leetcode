import threading
import queue
from typing import List

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def _crawl():
            nonlocal running
            while True:
                url = curQueue.get()
                if url is None:  # Sentinel value to stop the thread
                    break
                tmp = []
                for newUrl in htmlParser.getUrls(url):
                    if newUrl.split("http://")[1].split("/")[0] == domain and newUrl not in visited:
                        tmp.append(newUrl)
                        visited.add(newUrl)
                
                # Lock for modifying running count
                with lock:
                    # Add new URLs to the queue and increment running count
                    for newUrl in tmp:
                        curQueue.put(newUrl)
                        running += 1
                    # Decrement running count after processing
                    running -= 1
                nextQueue.put(tmp)

        curQueue, nextQueue, visited, domain = queue.Queue(), queue.Queue(), set([startUrl]), startUrl.split("http://")[1].split("/")[0]
        curQueue.put(startUrl)
        lock = threading.Lock()
        running = 1

        # Start worker threads
        threads = []
        for _ in range(5):
            thread = threading.Thread(target=_crawl, daemon=True)
            thread.start()
            threads.append(thread)

        # Wait for threads to finish
        while running > 0:
            # No need to use nextQueue here, it was only used to count running threads
            pass

        # Stop worker threads
        for _ in range(5):
            curQueue.put(None)  # Sentinel values to stop the threads
        for thread in threads:
            thread.join()

        return list(visited)
