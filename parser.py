# -*- coding: utf-8 -*-

from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import movieData
import os.path

print("Hello World")

moviePage = 'https://letterboxd.com/film/thief/'

#Open given movie page
movieUrl = urlopen(moviePage)
moviebs = BeautifulSoup(movieUrl, 'html.parser')

#Find the director page and open
directorPage = moviebs.find('a',{'itemprop':'director'})
directorUrl = urlopen('https://letterboxd.com' + directorPage['href'])
directorbs = BeautifulSoup(directorUrl, 'html.parser')

#<meta property="og:title" content="Midsommar (2019)" />
director = moviebs.find('meta',{'name': 'twitter:data1'})
director = director['content']
print("Directed by: {}" .format(director))

creditPages = directorbs.find_all('li',{'class':'poster-container'})
movieList = []
for credit in creditPages:
    currentItem = credit.find('div')
    currentItemTitle = currentItem['data-film-name']
    currentItemPage = 'https://letterboxd.com' + currentItem['data-target-link']
    currentItemUrl = urlopen(currentItemPage)
    currentItembs = BeautifulSoup(currentItemUrl, 'html.parser')
    
    print(currentItemTitle)
    movie = movieData.movieData(currentItembs)
    if len(movie.runtime) > 0:
        print(movie.runtime[0])
    print(movie.watches[0] + ' Watches')
    print(movie.rating[0] + ' out of 5')
    movieList.append(movie)

f = open('./Directors/' + director + '.txt', 'w')
f.write("Directed by: {}\n" .format(director))
for x in movieList:
    f.write(x.name + '\n')
    f.write(x.watches[0] + ' Watches\n')
    f.write(x.rating[0] + ' out of 5\n\n')
f.close()
        