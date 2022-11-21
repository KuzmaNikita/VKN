import requests, json
from bs4 import BeautifulSoup

# 1. Текстовий файл містить 10-12 URL-адрес веб-сторінок, записаних у 
# стовпчик. Користувач задає ключові слова (2-3). Програма повинна підрахувати 
# частоту кожного з цих слів на кожному з сайтів і результат записати в файл у 
# форматі JSON. 



def check_words(url):
    
        
        
        data = requests.get(url)
        if data.status_code == 200:
            print(f"Working on url {url} with status code {data.status_code}")
        else:
            print(f"Site isn't finded with status code - {data.status_code}")
        

        bs = BeautifulSoup(data.text, "html.parser").getText()
        bs = str(bs).lower()
        
        js[url] = {}
        

        
        for j in words:
            js[url][j] = bs.count(j.lower())
    

js = {}
words = []

for i in range(3):
    words.append(input("Введіть ключові слова: "))

with open("file.txt", "r") as f:
    urls = f.read().split("\n")

for i in urls:
    check_words(i)

with open("js.json", "w") as f:
    f.write(json.dumps(js))
