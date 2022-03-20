import requests
import opp_intern
from bs4 import BeautifulSoup
import mysql.connector
from datetime import datetime
import re
import uuid

headers1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}


with open("country.txt") as file:
        country_names = [line.rstrip() for line in file]
file.close()

with open("postlink_intern.txt") as file:
        url = [line.rstrip() for line in file]
file.close()






mysql = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="AHMAD9875321sam",
    database="scholaruni"
)

mycursor = mysql.cursor()

sql = "insert into scholarship_internship(slug,publisher,title,country,publish_date,add_date,post_content,star,feature_image) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
j = int(url[0])-int(url[1])-1
for lnk in url[2:]:
        j = j + 1
        val = opp_intern.get_post(lnk,country_names,image_name=str(j))
        print(lnk)
        try:
                mycursor.execute(sql,val)

                mysql.commit()
        except:
                continue
