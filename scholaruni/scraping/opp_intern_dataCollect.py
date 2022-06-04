import requests

from bs4 import BeautifulSoup

from datetime import datetime
import random


headers1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}

url = "https://opportunitiescorners.info/korean-government-scholarships/"


with open("country.txt") as file:
        country_names = [line.rstrip() for line in file]
file.close()


def get_data(url):
    html = requests.get(url, headers= headers1)
    soup = BeautifulSoup(html.text, "lxml")

    return soup

def get_post(url, country_names,image_name):
    soup = get_data(url)
    title = soup.find("h1", class_="entry-title").text
    date = soup.find("span", class_="td-post-date").text
    content = soup.find("div", class_="td-post-content tagdiv-type")
    try:
        content.div.decompose()
    except:
        print("no div found")
    try:
        content.blockquote.decompose()
    except:
        print("no decompose found")

    all = content.find_all(["h2","h3","p",'ol','ul'])

    for al in all:
        for a in al.findAll('a'):
            a['href'] = a['href'].replace("opportunitiescorners.info", "scholaruni.com/internships")
            a['href'] = a['href'].replace("opportunities_corner", "scholaruni")
            a['href'] = a['href'].replace("opportunitiescorners", "Scholaruni-106193131997924")
            a['href'] = a['href'].replace("https://www.facebook.com/groups/2197897307146576/", "https://www.facebook.com/groups/904226213585740")
            a['href'] = a['href'].replace("opcorner", "+6mfqmij5mVhkNTNl")

    post_text = ""
    for text in all:
        post_text = post_text + "\n" + str(text)

    
    titles = title.split()

    for country in titles:
        if country.lower() in country_names:
            country_n = country
            break
        else:
            country_n=""
    
    slug = url.rsplit('/')[-2]
    publisher = url.rsplit('/')[-3]
    now = datetime.now()
    add_date = now.strftime("%Y/%m/%d %H:%M:%S")
    star = random.randint(0, 5)
    img_link = f"uploads/post_images/internship/{slug}.jpg"
    return (slug,publisher,title,country_n,date,add_date,post_text,star,img_link)

