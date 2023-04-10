from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import time

browser = webdriver.Remote(
    command_executor='http://172.27.0.2:4444/wd/hub',
    options=webdriver.ChromeOptions()
)

url = 'https://www.facebook.com' + '/groups' + '/1260448967306807'
browser.get(url)

### tag to locate
article_class_ = "x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z"
content_class_ = "x11i5rnm xat24cr x1mh8g0r x1vvkbs xdj266r x126k92a"
more_content_class_ = "x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xzsf02u x1s688f"
text_dir_ = "auto"
comment_class_ = "x1n2onr6 x4uap5 x18d9i69 x1swvt13 x1iorvi4 x78zum5 x1q0g3np x1a2a7pz"
more_comment_class_ = "x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen x1s688f xi81zsa"

def check_articles_num(text:str):
    """
    This is an example of a function docstring.
    More descriptions go here.
    Args:
        param1 (str): Brower's current page source.
    Returns:
        int: Brower's current articles number.
        bool: True if successful, False otherwise.
    Raises:
        AttributeError: The ``Raises`` section is a list of all exceptions
        that are relevant to the interface.
        ValueError: If `param2` is equal to `param1`.
    """

    soup = BeautifulSoup(text, "html.parser")
    articles = soup.find_all("div", class_= article_class_)
    articles_num = len(articles)

    return articles_num, articles


time.sleep(3)
a0, b0 = check_articles_num(browser.page_source)
browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(1)
a1, b1 = check_articles_num(browser.page_source)
while True:
    if a1 > 5:
        break
    else:
        if a0 < a1:
            a0, b0 = a1, b1
            a1, b1 = check_articles_num(browser.page_source)
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

# for i in soup.find_all("div", class_= content_class_):
#     for j in i.find_all("div", dir=text_dir_):
#         print(j.text)

browser.quit()