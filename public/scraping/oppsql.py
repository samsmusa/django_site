import requests
from scraping import opp
from bs4 import BeautifulSoup
import pymysql.cursors
from datetime import datetime


def insertDataScholarship():
    headers1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1",
                "DNT": "1", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate"}

    with open("country.txt", encoding="utf-8") as file:
        country_names = [line.rstrip() for line in file]
    file.close()

    with open("postlink.txt", encoding="utf-8") as file:
        url = [line.rstrip() for line in file]
    file.close()

#     DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'scholaruni',
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#         'USER': 'root',
#         'PASSWORD': 'AHMAD9875321sam',
#     }
# }


    # connection = pymysql.connect(
    #     host="localhost",
    #     user="scholaez_adminScholar",
    #     passwd="qwertpoiuy@123@",
    #     database="scholaez_scholaruni_db",
    #     charset='utf8mb4')
    # print("db connect")

    connection = pymysql.connect(
        host="127.0.0.1",
        user="root",
        passwd="AHMAD9875321sam",
        database="scholaruni",
        charset='utf8mb4')
    print("db connect scholar")

    with connection:
        with connection.cursor() as cursor:
            sql = "insert into scholarship_scholarships(slug,publisher,title,country,publish_date,add_date,post_content,star,feature_image) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)" 
            j = int(url[0])-int(url[1])-1
            totalPost = 0

            for lnk in url[2:]:
                j = j + 1
                val = opp.get_post(
                    lnk, country_names, image_name=str(j))
                print(lnk)
                try:
                    cursor.execute(sql, val)

                    connection.commit()
                    requests.post(f"https://graph.facebook.com/106193131997924/feed?message={val[2]} &link=https://scholaruni.com&access_token=EAAJZChu8f8z4BACs3BwZBSNezZBZAaaE4ncTg0OADFcPaosQdpS7E6hGdLrLGvHtIBwwhRQGcXRSlwD37eId0ds33nZAawSWVask3cNp8ypto0qNglUVnYz5I40tb87BikbJ6PeuBihRHgBc0ENw7kmmG7w1gdZCBCm02QJQxoDGLx773LQYAYFjJwAu7RoVvF1dcOZALjk6QZDZD")
                    print('add')
                    totalPost += 1
                except:
                    continue
    return totalPost
