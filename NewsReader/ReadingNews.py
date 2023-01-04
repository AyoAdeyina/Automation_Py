import requests
from sys import argv

API_KEY = 'a8a5ec29b03842428a92444a17ffc19d'

URL = ('https://newsapi.org/v2/top-headlines?')

def get_articles_by_section(section):
    query_params = {
        "section" : section,
        "sortBy" : "top",
        "country" : "ae",
        "apiKey" : API_KEY
    }
    return _get_news(query_params)


def get_articles_by_query(query):
    query_params = {
        "q" : query,
        "sortBy" : "top",
        "country" : "ae",
        "apiKey" : API_KEY
    }
    return _get_news(query_params)



def _get_news(params):
    action = requests.get(URL, params = params)

    newsArticles = action.json()['newsArticles']

    res = []

    for article in newsArticles:
        res.append({"title" : article["title"], "url": article["url"]})

    for result in res:
        print(result["title"])
        print(result["url"])
        print('')

def get_sources_by_section(section):
    url = 'https://newsapi.org/v2/top-headlines?'
    query_params = {
        "section" : section,
        "language" : "en",
        "apiKey" : API_KEY
    }

    action = requests.get(url, params = query_params)

    sources = action.json()["sources"]

    for source in sources:
        print(source["name"])
        print(source["url"])


if __name__ == "__main__":
    print(f"Receiving news for {argv[1]}...\n")
    get_articles_by_section(argv[1])
    print(f"Successfully acquired top {argv[1]} headlines")