# coding=utf-8
from pyquery import PyQuery

def to_tryurl_list():
    """ 要尝试的抓取的url """
    total_page_number = 50
    for page_number in xrange(1, total_page_number):
        url = "http://blog.jobbole.com/tag/python/page/" + str(page_number)
        yield url

def extract_content():

    HTTP404_ERROR = "HTTP Error 404: Not Found"
    for tryurl in to_tryurl_list(): 
        url_handle = None
        try:
            url_handle = PyQuery(tryurl) 
        except Exception as e:
            if str(e) == HTTP404_ERROR:
                break

        article_titles = url_handle('.grid-8 .meta-title')
        for article_title in article_titles:
            article_title = PyQuery(article_title)
            sub_content = (article_title.text(), article_title.attr("href"))
            yield sub_content

if __name__ == "__main__":
    for content in extract_content():
        print content

