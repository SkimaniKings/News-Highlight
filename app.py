from flask import Flask
from newsapi import NewsApiClient

app = Flask(__name__)

@app.route('/')
def index():
    
    
    """
 A view root page function that returns the index page and its data
    """
    newsapi = NewsApiClient(api_key="cca440cda74d458a8d8d34a747f29ac8")
    topheadlines = newsapi.get_top_headlines(sources="abc-news")
    
    articles = topheadlines['articles']
    
    heading= []
    news = []
    image = []
    date = []
    
    for i in range(len(articles)):
        myarticles = articles[i]
        
        news.append(myarticles['tittle'])
        news.append(myarticles['description'])
        news.append(myarticles['urlToImage'])
        news.append(myarticles['publishedAt'])
        
 