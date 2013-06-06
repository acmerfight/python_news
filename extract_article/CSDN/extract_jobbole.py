# coding=utf-8
from pyquery import PyQuery

def to_tryurl_list():
    """ 要尝试的抓取的url """
    total_page_number = 1000000 
    for page_number in xrange(1, total_page_number):
        url = "http://www.csdn.net/article/tag/python/" + str(page_number)
        yield url

def extract_content():

    for tryurl in to_tryurl_list(): 
        url_handle = PyQuery(tryurl) 

        article_titles = url_handle('.content .unit h1')
        #print article_titles
        if not article_titles:
            break
        for article_title in article_titles:
            article_title = PyQuery(article_title)
            sub_content = (article_title.text(), article_title.attr("href"))
            print article_title.text(), article_title.attr("[href]")

if __name__ == "__main__":
    extract_content()
