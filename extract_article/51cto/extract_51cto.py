# coding=utf-8
from pyquery import PyQuery

def to_tryurl_list():
    """ 要尝试的抓取的url """
    total_page_number = 1000000 
    for page_number in xrange(1, total_page_number):
        url = "http://developer.51cto.com/col/1455/list_1455_{number}.htm".format(number=page_number)
        yield url

def extract_content():
    """ 抓取需要的文章题目和链接 """
    for tryurl in to_tryurl_list(): 
        complete_page = PyQuery(tryurl) 

        article_titles = complete_page('.main-left .list_leftcont .font20')
        if not article_titles:
            break
        for article_title in article_titles:
            article_title = PyQuery(article_title)
            sub_content = (article_title.text(), article_title.attr("href"))
            print article_title.text(), article_title.find("a").attr('href')

if __name__ == "__main__":
    extract_content()
