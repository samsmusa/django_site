from email import header
import requests
from bs4 import BeautifulSoup
import time

def linkGenerationIntern():

    start = time.time()
    print("__________")
    print(start)
    print("__________")

    headers1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}


    def get_data(url):
        html = requests.get(url, headers= headers1)
        soup = BeautifulSoup(html.text, "lxml")

        return soup


    with open('last_post_intern.txt', 'r') as f:
        lines = f.readlines()
        last_link = lines[-1]
        j = int(lines[-2])
        k = int(lines[-2])
    f.close()
    
    print(j, last_link)


    url = "https://opportunitiescorners.info/category/scholarships/page/2/"

    links = []
    image_links = []
    for i in range(1,20):
        print(str(i)+" page")
        url = "https://opportunitiescorners.info/category/internships/page/"+str(i)+"/"
        soup = get_data(url)
        div = soup.find("div",class_="td-ss-main-content")
        block = div.find_all("div", class_="td-block-span6")
        broken = False

        i=0
        for tags in block:
            link = tags.a
            links.append(link['href'])
                
                
            print(links[-1]==last_link)
            if links[-1]==last_link:
                links.pop()
                broken = True
                break
            i = i+1
            j = j+1
        if broken:
            break

    with open("last_post_intern.txt", "a") as file_object:
        # Append 'hello' at the end of file
        if(k != j):
            file_object.write("\n"+str(j))
            file_object.write("\n"+links[0])
    file_object.close


    


    post_link = str(j)+"\n"+str(i)

    for text in links:
        post_link = post_link + "\n" + str(text.lower())

    with open("postlink_intern.txt", "w", encoding='utf-8') as file:
        
        file.write(post_link)
    file.close()

