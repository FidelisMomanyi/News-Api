import urllib.request,json
from .models import Source,Article


Source = Source

Article = Article

#getting api key
# api_key = None


# #news base url
# news_source_url = None

# article_url = None

def configure_request(app):
    global api_key, base_url,news_sources_url,articles_url

    api_key = app.config['SOURCE_API_KEY']

    #news base url
    news_sources_url = app.config["NEWS_SOURCES_API_BASE_URL"]

    articles_url =app.config['EVERYTHING_SOURCE_API_URL']

def get_sources(category):
    '''
    Function to get json response 
    '''
    get_source_url = news_sources_url.format(category,api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
           source_results_list = get_source_response['sources']
           source_results = process_source_results(source_results_list)

    return source_results


def process_source_results(source_list):
    '''
    Function  that processes the result and transform them to a list of Objects

    '''
    source_results = []
    for source_item in source_list:
        
        id = source_item.get('id')
        name = source_item.get('name')
        author = source_item.get('author')
        title = source_item.get('title')
        author = source_item.get('author')
        description = source_item.get('description')
        publishedAt = source_item.get('publishedAt')
        Image = source_item.get('imageUrl')
        url = source_item.get('url')

        source_object = Source(id, name, author, title,
                                description, publishedAt, Image, url)
        source_results.append(source_object)

    return source_results


def get_article(id):
    '''
    Function to get json response 
    '''
    get_article_url = article_url.format(id, api_key)

    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        article_results = None

        if get_article_response['articles']:
           article_results_list = get_article_response['articles']
           article_results = process_source_results(article_results_list)

    return article_results


def process_article_results(article_list):
    '''
    Function  that processes the result and transform them to a list of Objects

    '''
    article_results = []
    for article_item in article_list:
        name = article_item.get('name')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        publishedAt = article_item.get('publishedAt')
        imageUrl = article_item.get('imageUrl')
        url = article_item.get('url')
        
        article_object = Article(
            name, author, title, description, publishedAt, imageUrl, url)
        article_results.append(article_object)

    return article_results
