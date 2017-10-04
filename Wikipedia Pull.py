import wikipedia as wiki
import bs4 as bs
import urllib.request
import simplejson


#input name
movie_name_main = "http://www.imdb.com/title/tt0416449/?ref_=fn_al_tt_1"
movie_name_extra = "http://www.imdb.com/title/tt0416449/fullcredits?ref_=tt_ov_st_sm"

#pull url from wikipedia
main_sauce = urllib.request.urlopen(movie_name_main).read
main_soup = bs.BeautifulSoup(main_sauce(), "lxml")

extra_sauce = urllib.request.urlopen(movie_name_extra).read
extra_soup = bs.BeautifulSoup(extra_sauce(), "lxml")

#Variables
#print(main_soup)
"""name = main_soup.title.text
name = name.replace('(****) - IMDb', '')[:-14]

director = main_soup.find("span", {"itemprop":"director"}).get_text()

producer = main_soup.find("span", {"itemprop":"producer"})

#producer
writer
top_billed
#music
#cinematography
#editor
release_date
run_time
budget
box_office
mpaa_rating
animated
family_friendly
rating
genre"""


