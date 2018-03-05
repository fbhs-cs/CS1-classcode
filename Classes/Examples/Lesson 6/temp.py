

import urllib.request
url = 'https://www.brainyquote.com/topics/computer_science?vm=l'
req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) 
html = urllib.request.urlopen(req).read().splitlines()

quotes = []
for i in range(len(html)):
    if b"view quote" in html[i]:
        start = html[i].index(b'quote">') + 7
        end = html[i].index(b'</a>')
        author_s = html[i+1].index(b'or">') + 4
        author_e = html[i+1].index(b'</a>')
        quote = html[i][start:end].decode("utf-8")
        author = html[i+1][author_s:author_e].decode("utf-8")
        quotes.append( quote+ " - " + author )
        
for i in range(len(quotes)):
    quotes[i] = quotes[i].replace('&#39;',"'") 

for quote in quotes:
    print(quote + "\n")
  
    