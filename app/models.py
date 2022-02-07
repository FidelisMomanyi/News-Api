class Source:
    
    """
    source class defining source objects
    """

    def __init__(self, id, name, author, title, description, publishedAt, Image, url):
        self.id = id
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.publishedAt = publishedAt
        self.Image = Image
        self.url = url



class Article:
    
    """
    article class defining article objects

    """
    all_article = []

    def __init__(self, name, author, title, description, publishedAt, imageUrl, url):

        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.publishedAt = publishedAt
        self.imageUrl = imageUrl
        self.url = url

    def save_article(self):
        Article.all_article.append(self)


    @classmethod
    def clear_article(cls):
        Article.all_article.clear()

    @classmethod
    def get_article(cls,id):

        response = []

        for article in cls.all_article:
            if article.movie_id == id:
                response.append(article)

        return response