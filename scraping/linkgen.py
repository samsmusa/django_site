from email import header
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
import pandas as pd
import time
import re


start = time.time()
print("__________")
print(start)
print("__________")

headers1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}


def get_data(url):
    html = requests.get(url, headers= headers1)
    soup = BeautifulSoup(html.text, "lxml")

    return soup


with open('last_post.txt', 'r') as f:
    lines = f.readlines()
    last_link = lines[-1]
    j = int(lines[-2])
f.close()


url = "https://opportunitiescorners.info/category/scholarships/page/2/"

links = []
image_links = []
for i in range(1,20):
    print(str(i)+" page")
    url = "https://opportunitiescorners.info/category/scholarships/page/"+str(i)+"/"
    soup = get_data(url)
    div = soup.find("div",class_="td-ss-main-content")
    block = div.find_all("div", class_="td-block-span6")
    broken = False

    i=0
    for tags in block:
        link = tags.a
        image = link.findAll("img")
        # print(img['href'])
        
        li = image[1]['src']
        lik = str(li)
        img_lk = lik.replace("100x70.jpg","356x220.jpg")

        # print(lik)
        
        
        st = requests.get(img_lk, headers= headers1)
        print(st.status_code)
        slug = str(link['href']).rsplit('/')[-2]
        print(str(link['href']))
        if st.status_code == 200:
            with open(f"image/image/{slug}.jpg", 'wb') as f:
                for chunk in st:
                    f.write(chunk)
            links.append(link['href'])
            image_links.append(img_lk)
            
            
            print(links[-1]==last_link)
            if links[-1]==last_link:
                links.pop()
                broken = True
                break
            i = i+1
            j = j+1
    if broken:
        break

with open("last_post.txt", "a") as file_object:
    # Append 'hello' at the end of file
    file_object.write("\n"+str(j))
    file_object.write("\n"+links[0])
file_object.close


image_link = ""
for text in image_links:
    image_link = image_link + "\n" + str(text.lower())
with open("imagelink.txt", "w", encoding='utf-8') as file:
    # for text in country:
    file.write(image_link)
file.close()


post_link = str(j)+"\n"+str(i)

for text in links:
    post_link = post_link + "\n" + str(text.lower())

with open("postlink.txt", "w", encoding='utf-8') as file:
    
    file.write(post_link)
file.close()

