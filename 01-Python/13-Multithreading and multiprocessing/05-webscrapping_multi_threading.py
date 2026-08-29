'''
Real-World Example: Multithreading for I/O-bound Tasks
Scenario: Web Scraping
Web scraping often involves making numerous network requests to 
fetch web pages. These tasks are I/O-bound because they spend a lot of
time waiting for responses from servers. Multithreading can significantly
improve the performance by allowing multiple web pages to be fetched concurrently.

'''

'''

https://python.langchain.com/v0.2/docs/introduction/

https://python.langchain.com/v0.2/docs/concepts/

https://python.langchain.com/v0.2/docs/tutorials/
'''

import threading
import requests ##This is a Python library used to send HTTP requests.
from bs4 import BeautifulSoup ##BeautifulSoup helps Python read and extract useful information from that HTML

urls=[
'https://python.langchain.com/v0.2/docs/introduction/',

'https://python.langchain.com/v0.2/docs/concepts/',

'https://python.langchain.com/v0.2/docs/tutorials/'

]
##BeautifulSoup takes that HTML and makes it easier to work with 'html.parser' 
def fetch_content(url):
    response=requests.get(url)

    soup=BeautifulSoup(response.content,'html.parser')
    print(f'Fetched {len(soup.text)} characters from {url}')

threads=[]

for url in urls:
    thread=threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All web pages fetched")
