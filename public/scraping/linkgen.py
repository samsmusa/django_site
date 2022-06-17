import requests
from bs4 import BeautifulSoup
import datetime

x = datetime.datetime.now()


def linkGenerationScholarship():

    
    print("__________")
    print(x)
    print("__________")

    headers1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}


    def get_data(url):
        html = requests.get(url, headers= headers1)
        soup = BeautifulSoup(html.text, "lxml")

        return soup


    with open('last_post.txt', 'r', encoding="utf-8") as f:
        lines = f.readlines()
        last_link = lines[-1]
        j = int(lines[-2])
        k = int(lines[-2])
    f.close()


    # url = "https://opportunitiescorners.info/category/scholarships/page/2/"
    links = []
    for i in range(1,20):
        print('hitted')
        print(str(i)+" page")
        url = f"https://opportunitiescorners.info/category/fully-funded-scholarships/page/{i}/"
        soup = get_data(url)
        div = soup.find("div",class_="td-ss-main-content")
        # print(div)
        block = div.find_all("div", class_="td-block-span6")

        broken = False
        i=0
        print(i)
        for tags in block:
            link = tags.a
            
            links.append(link['href'])
            print(link['href'])
                
                
            print(links[-1]==last_link)
            if links[-1]==last_link:
                links.pop()
                broken = True
                break
            i = i+1
            j = j+1
        if broken:
            break
    print(links)
    with open("last_post.txt", "a", encoding="utf-8") as file_object:
        # Append 'hello' at the end of file
        print(link[0])
        print(k, j)
        if k != j:
            file_object.write("\n"+str(j))
            file_object.write("\n"+links[0])
            print(link[0])
    file_object.close




    post_link = str(j)+"\n"+str(i)

    for text in links:
        post_link = post_link + "\n" + str(text.lower())

    with open("postlink.txt", "w", encoding='utf-8') as file:
        
        file.write(post_link)
    file.close()
    print('linkgen_schol_end')

