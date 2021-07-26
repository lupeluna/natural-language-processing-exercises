from requests import get
from bs4 import BeautifulSoup
import os


def get_blog_articles(url):
    blog_dict = {}
    # otherwise go fetch the data
    headers = {'User-Agent': 'Codeup Data Science'}
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.text)
    article = soup.find('div', class_='jupiterx-post-content')
    title = soup.find('h1', class_='jupiterx-post-title')
    blog_dict = {'title': title.text,
                'content': article.text}
    return blog_dict






def get_post(urls):
    
    '''this function takes in a list of urls and then iterates through each url and pulls the title of the blog post and the content. That information is the appended into an empty dictionary. That dictionary is returned as pandas data frame'''
    
    # create empty list
    
    empty_d = []
    
    #create the for loop that uses beautiful soup to pull information
    
    for url in urls:
        
        headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
        response = requests.get(url, headers=headers)
        html = response.text
        soup = bs4.BeautifulSoup(html)
    
        article_div = soup.select(".jupiterx-main-content")[0]
        title = article_div.find('h1').text
        body_container = article_div.select('.jupiterx-post-content.clearfix')[0]
        body_content = body_container.text
       
        content = { 'title': title, 
                    'content': body_content}
        
        empty_d.append(content)

        
    # create data frame 
    df = pd.DataFrame(empty_d)
    
    return df



def get_article(article, category):
    # Attribute selector
    title = article.select("[itemprop='headline']")[0].text
    
    # article body
    content = article.select("[itemprop='articleBody']")[0].text
    
    output = {}
    output["title"] = title
    output["content"] = content
    output["category"] = category
    
    return output



def get_articles(category, base ="https://inshorts.com/en/read/"):
    """
    This function takes in a category as a string. Category must be an available category in inshorts
    Returns a list of dictionaries where each dictionary represents a single inshort article
    """
    
    # We concatenate our base_url with the category
    url = base + category
    
    # Set the headers
    headers = {"User-Agent": "Mozilla/4.5 (compatible; HTTrack 3.0x; Windows 98)"}

    # Get the http response object from the server
    response = get(url, headers=headers)

    # Make soup out of the raw html
    soup = BeautifulSoup(response.text)
    
    # Ignore everything, focusing only on the news cards
    articles = soup.select(".news-card")
    
    output = []
    
    # Iterate through every article tag/soup 
    for article in articles:
        
        # Returns a dictionary of the article's title, body, and category
        article_data = get_article(article, category) 
        
        # Append the dictionary to the list
        output.append(article_data)
    
    # Return the list of dictionaries
    return output



def get_all_news_articles(categories):
    """
    Takes in a list of categories where the category is part of the URL pattern on inshorts
    Returns a dataframe of every article from every category listed
    Each row in the dataframe is a single article
    """
    all_inshorts = []

    for category in categories:
        all_category_articles = get_articles(category)
        all_inshorts = all_inshorts + all_category_articles

    df = pd.DataFrame(all_inshorts)
    return df





