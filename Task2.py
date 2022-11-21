import requests, random
from bs4 import BeautifulSoup

# 2. Написати програму для завантаження з веб-сторінки 3-4 випадкових 
# зображень, тематика яких пов´язана з розробкою програмного забезпечення. 
# Сайт знайти самостійно. 


def download_img(url, name):
    print(url)
    img = requests.get(url)

    # Зберігаємо нашу картинку в поточну папку
    with open(name, 'wb') as f: 
        f.write(img.content)


url = "https://unsplash.com/s/photos/programming-language"
req = requests.get(url).text
bs = BeautifulSoup(req, "html.parser")


imgs = bs.find("div", {"class": "mItv1"}).findAll("img")


for i in range(4):
    download_img(random.choice(imgs)["src"], f"image{i}.jpeg")

