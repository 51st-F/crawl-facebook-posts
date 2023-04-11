from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import time

### You may have to check you ip in container names called 'crawl-facebook-posts-chrome_standalone-1' first
browser = webdriver.Remote(
    command_executor='http://172.27.0.2:4444/wd/hub',
    options=webdriver.ChromeOptions()
)

url = 'https://www.facebook.com' + '/groups' + '/1260448967306807'
browser.get(url)

def check_articles_num(text: str):
    """
    Use the div class below to sperate articles from raw html.
    .
    Args:
        text (str): Brower's current page source.
    Returns:
        articles_num (int): Brower's current articles number.
        articles (list): After using beautifulSoup.find_all(), it generate article's full html to list.
    Raises:
        If articles_num equals zero, 
        you may have to check whether method of locating content is correct or other unexpected problems.
    """
    articles_div_class = "x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z"

    soup = BeautifulSoup(text, "html.parser")
    articles = soup.find_all("div", class_= articles_div_class)
    articles_num = len(articles)

    if articles_num == 0:
        ValueError('Can not find any facebook articles from your input')

    return articles_num, articles

time.sleep(2)
a0, b0 = 0, []
a1, b1 = check_articles_num(browser.page_source)
articles_wanted = 50

while True:
    ### Remove the first if-else statement then it'll continuous crawl articles till articles number is not increased after scrolling down.
    if a1 > articles_wanted:
        break
    else:
        if a0 < a1:
            a0, b0 = a1, b1
            a1, b1 = check_articles_num(browser.page_source)
            time.sleep(1)
            browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        else:
            time.sleep(3)
            browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            a1, b1 = check_articles_num(browser.page_source)
            if a0 < a1:
                a0, b0 = a1, b1
                a1, b1 = check_articles_num(browser.page_source)
                browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                continue
            else:
                break

def articles_to_list(text: list):
    """
    Use the info provided in ('div', {"aria-label":False, "role":"article", "class":"x1a2a7pz"})['aria-describedby'] to locating content and make it to DataFrame.

    Args:
        text (str): Brower's current page source.
    Returns:
        articles_num (int): Brower's current articles number.
        articles (list): After using beautifulSoup.find_all(), it generate article's full html to list.
    Raises:
        If articles_df's row equals zero,
        you may have to check whether method of locating content is correct or other unexpected problems.
    """
    article_list = []
    for i in text:
        for j in i.find_all('div', {"aria-label":False, "role":"article", "class":"x1a2a7pz"}):
            for m in j['aria-describedby'].split(' '):
                for n in j.find_all("div", {"id":f"{m}", "data-ad-preview":True}):
                    try:
                        article_content = n.text
                    except:
                        pass
                for n in j.find_all("div", {"id":f"{m}", "class":"x1iorvi4 x1pi30zi x1l90r2v x1swvt13"}):
                    try:
                        article_content = n.text
                    except:
                        pass
                for n in j.find_all('span', {'id':f'{m}'}):
                    for o in n.find_all('a', {'role':'link'}):
                        try:
                            article_link = o['href']
                            article_link_split = article_link.split('?')[0].split('/')
                            if article_link_split[-1] == '':
                                article_id = article_link_split[-2]
                            else:
                                article_id = article_link_split[-1]
                        except:
                            pass
        article_list.append([article_id, article_link, article_content])

    articles_df = pd.DataFrame(article_list, columns=['id','link','content'])

    if articles_df.shape[0] == 0:
        ValueError('Can not find the contents expected from articles')
    
    return articles_df

df = articles_to_list(b1)
df.to_csv('demo.csv',encoding='utf-8', index=False)

browser.quit()