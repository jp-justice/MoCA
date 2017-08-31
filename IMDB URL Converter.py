import bs4 as bs
import urllib.request
import sys

movie_url = input("What is your movie's URL?\n")
sauce = urllib.request.urlopen(movie_url).read
soup = bs.BeautifulSoup(sauce(), "lxml")


director = soup.find('span', {'class': 'itemprop', 'itemprop': 'name'})
year = soup.find('a', {'title': 'See more release dates'})
name = soup.title.string
name = name.replace('*', '')[:-8]
name = name.replace('*', '')[:len(name)-5]


print("Your movie's name is " + name)
print("Your movie's director is " + director.text)
print("Your movie's release date was "+ year.text)

sys.exit()
