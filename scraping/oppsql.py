import requests
import opp
from bs4 import BeautifulSoup
import mysql.connector
from datetime import datetime
import re
import uuid

headers1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}


with open("country.txt") as file:
        country_names = [line.rstrip() for line in file]
file.close()


url = ["https://opportunitiescorners.info/korean-government-scholarships/","https://opportunitiescorners.info/government-of-azerbaijan-scholarship/","https://opportunitiescorners.info/canadian-government-scholarships/","https://opportunitiescorners.info/fully-funded-european-scholarships/","https://opportunitiescorners.info/start-your-degree-in-canada-without-ielts/","https://opportunitiescorners.info/rotary-peace-scholarship/","https://opportunitiescorners.info/spanish-government-scholarships/","https://opportunitiescorners.info/scholarships-deadline-in-february/","https://opportunitiescorners.info/australian-awards-scholarships/","https://opportunitiescorners.info/government-of-netherlands-scholarships/","https://opportunitiescorners.info/fully-funded-australian-scholarships/","https://opportunitiescorners.info/korean-government-scholarships/","https://opportunitiescorners.info/fulbright-scholarship-in-usa/","https://opportunitiescorners.info/scholarships-to-study-in-italy/","https://opportunitiescorners.info/welcome-to-canada-the-land-of-opportunities/"]



mysql = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="AHMAD9875321sam",
    database="scholaruni"
)

mycursor = mysql.cursor()

sql = "insert into scholarship_scholarships(slug,publisher,title,country,publish_date,add_date,post_content) values(%s,%s,%s,%s,%s,%s,%s)"

for lnk in url:
        val = opp.get_post(lnk,country_names)
        print(lnk)
        try:
                mycursor.execute(sql,val)

                mysql.commit()
        except:
                continue
