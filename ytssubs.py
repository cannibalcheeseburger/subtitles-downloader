import wget
import imdb
import requests
from bs4 import BeautifulSoup as soup
import sys


ytsbase = 'https://yts-subs.com/movie-imdb/'
yifybase = 'https://www.yifysubtitles.com'

title = " ".join(sys.argv[1:])
print(title)
if title.strip() == "":
    title = input('Enter title: ')

ia = imdb.IMDb()
movie_obj = ia.search_movie(title)
for mov in movie_obj:
    el = ia.get_movie(mov.movieID)
    
    title = el.get('title')
    year = str(el.get('year'))
    print("Title: "+title)
    print("Year: "+year)
    print("PLOT:\n"+el.get('plot')[0])
    choice = input("\nIs this it?(ENTER for yes/n for next)").lower()
    if choice == 'n':
        continue
    imdbid = "tt" + mov.movieID 
    break

ytsres = requests.get(ytsbase+imdbid).text
page_soup = soup(ytsres,'html.parser')

engsub = []
rowscont = page_soup.find_all('tr')
for rows in rowscont:
    colcont = rows.find_all('td')[1:3]
    for column in colcont:
        if column.text.lower().strip() == 'english':
            engsub.append(rows.find('a')['href'])
print(engsub)

# change is necessary
if len(engsub)>10:
    engsub = engsub[:10]
for sub in engsub:
    wget.download(yifybase +sub[:9]+sub[10:]+'.zip','./subs/'+sub[11:]+'.zip')
