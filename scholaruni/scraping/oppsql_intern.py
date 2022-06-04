import requests
from scraping import opp_intern_dataCollect
from bs4 import BeautifulSoup
import pymysql.cursors
from datetime import datetime


def insertData():
    headers1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1",
                "DNT": "1", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate"}

    with open("country.txt") as file:
        country_names = [line.rstrip() for line in file]
    file.close()

    with open("postlink_intern.txt") as file:
        url = [line.rstrip() for line in file]
    file.close()

    connection = pymysql.connect(
        host="127.0.0.1",
        user="root",
        passwd="AHMAD9875321sam",
        database="scholaruni",
        charset='utf8mb4')
    print("db connect")
    with connection:
        with connection.cursor() as cursor:

            sql = "insert into scholarship_internship(slug,publisher,title,country,publish_date,add_date,post_content,star,feature_image) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            j = int(url[0])-int(url[1])-1
            totalPost = 0
            for lnk in url[2:]:
                j = j + 1
                val = opp_intern_dataCollect.get_post(
                    lnk, country_names, image_name=str(j))
                print(lnk)
                try:
                        cursor.execute(sql, val)
                        connection.commit()
                        requests.post(f"https://graph.facebook.com/106193131997924/feed?message={val[2]} &link=https://scholaruni.com&access_token=EAAJZChu8f8z4BABZAl5tXBHA9X8goDmUQZAe3Jq9ileZCrgbCwvEi199ZAgQ4O8B8AbZB19Mn65AbCYSGmbnypchRpxoYNFXOXF5ZC7d8IB5bvqRxqY3iGH80Vw4IV40EHt0e1LNd5EVfZADbqHxrO48JfqZBcYI7UZBtFkNk5295oaZCw4zrKtZBqHlGvhjQkVRNId7ItBZByVgIWi67q3uqVL1n")
                        print('add')
                        totalPost += 1
                except:
                    continue
    return totalPost
