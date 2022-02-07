import os

class Config:

    """
    General configuration parent class
    """
    NEWS_SOURCES_API_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'

    EVERYTHING_SOURCE_API_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'
    
    SOURCE_API_KEY = os.environ.get('SOURCE_API_KEY')

class ProdConfig(Config):
 pass


class DevConfig(Config):
 DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}