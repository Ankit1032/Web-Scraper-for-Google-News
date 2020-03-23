from bs4 import BeautifulSoup
import requests
import csv


def searchWord(headline,summary,word):
    res1 = headline.find(word)
    res2 = summary.find(word)

    if(res1 != -1):
        print("\"",word,"\""," found in the string : ",headline)
        print()

    if(res2 != -1):
        print("\"",word,"\""," found in the string : ",summary)
        print()


def scrapeNews(word=None):
    #used to store the scraped data in csv file
    csv_file = open('news_scrape.csv','w',encoding='utf-8')
    csv_writer = csv.writer(csv_file)

    #the name of the columns
    csv_writer.writerow(['HeadNews','SubNews'])

    #looping through all the <article> artibutes
    for arti in soup.find_all('div',class_='xrnccd F6Welf R7GTQ keNKEd j7vNaf'):

        #headline of the article
        headline = arti.h3.a.text
        #print(headline)

        #summary
        summary = arti.find('div',class_='SbNwzf').h4.a.text
        #print(summary)

        #pass the headline and summary to search the user given Word
        if word is not None:
            searchWord(headline,summary,word)

        csv_writer.writerow([headline, summary])

    csv_file.close()


#.get() sends a response from which we extract text and store in source
source = requests.get('https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen').text

#soup is the object which takes source and the parser
soup = BeautifulSoup(source,'lxml')

var = int(input("Do you want to search a word while scraping? : press 1 for yes, press 0 for no: "))

if(var == 1):
    #input word to be searched
    word = input("Input the word to be searched: ")
    scrapeNews(word)
else:
    scrapeNews()

print("|| Data is totally Scraped from the website and the CSV file is created! ||")
print()
