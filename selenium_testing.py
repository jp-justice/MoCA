from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import bs4 as bs
import urllib.request
link_list = ["http://www.imdb.com/title/tt0062622/"]
source_list = []
#Scrape Google for IMDB links to all movies
def get_source():
    with open("Formatted Movie Data.txt", 'r') as r:
        content = r.readlines()
        content = [i.strip(",\n") for i in content]
        source_list = list(content)

def get_scarpe():
    driver = webdriver.Chrome("C:\Program Files (x86)\Python36-32\selenium\webdriver\chromedriver_win32\chromedriver.exe")
    for i in source_list:
        driver.get("http://www.google.com")
        assert "Google" in driver.title
        search_box = driver.find_element_by_id("lst-ib")
        search_box.send_keys(i + " IMDB")
        search_box.send_keys(Keys.RETURN)
        link = driver.find_element_by_class_name("_Rm")
        link_list.append(link.text)
        time.sleep(1)

output = list(zip(source_list, link_list))
#print(output)

#Scrape IMDB pages for variables
for i in (link_list):
    main_sauce = urllib.request.urlopen(i).read
    main_soup = bs.BeautifulSoup(main_sauce(), "lxml")
    name = main_soup.title.text
    name = name.replace('(****) - IMDb', '')[:-14]
    director = main_soup.find("span", {"itemprop": "director"}).get_text()
    #producer = main_soup.find("span", {"itemprop": "producer"})
    writer = main_soup.find("span", {"itemprop": "creator"}).get_text()
    writer = writer.replace(' (screenplay),', '')
    top_billed = main_soup.find("span", {"itemprop": "actors"}).text
    top_billed = top_billed.replace(',', '')
    release_date = main_soup.find("h4", {"class": "inline"}).get_text()
    print(name, director, writer, top_billed, release_date)
