import os
from googlesearch import search

try:
    from util.search_engine_scraper.engine import SearchEngine, SearchResult
    from util.search_engine_scraper.config import HEADERS, USER_AGENTS
except ImportError:
    from engine import SearchEngine, SearchResult
    from config import HEADERS, USER_AGENTS

from typing import List

class Google(SearchEngine):
    def __init__(self) -> None:
        super().__init__()
        self.proxy = os.environ.get("HTTPS_PROXY")
    
    async def search(self, query: str, num_results: int) -> List[SearchResult]:
        results = []
        try:
            ls = search(query, advanced=True, num_results=num_results, timeout=3, proxy=self.proxy)
            for i in ls:
                results.append(SearchResult(title=i.title, url=i.url, snippet=i.description))
        except:
            pass
        return results