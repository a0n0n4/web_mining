from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def depthFirstSearch(url):
    global pages, searchWord, totalPages

    if url in pages:
        return
    pages.add(url)
    totalPages-=1
    print(url)
    html = urlopen(url.format(url))
    bs = BeautifulSoup(html, 'html.parser')
    s=str(bs).lower()
    i=s.find(searchWord)
    if i!=-1:
        print("found",searchWord,"in",url)
        print(s[max(0,i-100):min(len(s)-1,i+100)])
        print('-'*20)
        totalPages=-1
        return
    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if totalPages==-1:
            return
        if totalPages==0:
            print("searching terminated due to max pages reached")
            totalPages-=1
            return
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                newPage="https://en.wikipedia.org/"+newPage
                depthFirstSearch(newPage)

pages = set()
searchWord=input("Enter the word to search: ")
inputUrl=input("Enter the url to start with: ")
totalPages=int(input("Enter the number of pages to search: "))
print("searching for",searchWord,"in",inputUrl,"for",totalPages,"pages\n\n")
depthFirstSearch(inputUrl)