# working with api
# Google books api url
# https://www.googleapis.com/books/v1/volumes?q=isbn:9781801071109
import json
import textwrap
import urllib.request

with urllib.request.urlopen('https://www.googleapis.com/books/v1/volumes?q=isbn:9781801071109') as f:
    txt = f.read()
    decoded_txt = txt.decode("utf-8")
    #print(textwrap.fill(decoded_txt, width=50))

# json
obj = json.loads(decoded_txt)
book_title = obj['items'][0]['volumeInfo']['title']
book_subtitle = obj['items'][0]['volumeInfo']['subtitle']
book_authors = obj['items'][0]['volumeInfo']['authors']
book_description = obj['items'][0]['volumeInfo']['description']
book_snippet = obj['items'][0]['searchInfo']['textSnippet']
date_published = obj['items'][0]['volumeInfo']['publishedDate']

# print book basic info


def book_details():
    print(book_title)
    print(book_subtitle)
    print(book_authors)
    print(date_published)
    print(book_snippet)
    print(textwrap.fill(book_description, width=120, initial_indent="    "))


book_details()
