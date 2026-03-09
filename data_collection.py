from duckduckgo_search import DDGS

def search_sector_news(sector):
    results = []
    query = f"{sector} sector India news"

    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=5):
            results.append(r["title"] + " - " + r["body"])

    return results