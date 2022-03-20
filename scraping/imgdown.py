import requests
import urllib3.request
# imgURL = "http://site.meishij.net/r/58/25/3568808/a3568808_142682562777944.jpg"

import time

headers1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
headers2 = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/97.0.1072.69"}



with open("imagelink.txt") as file:
        img_link = [line.rstrip() for line in file]
file.close()

# print(img_link)

# for i,link in enumerate(img_link[::-1]):
#     print(i)
#     response = requests.get(link,headers=headers1,stream=True)
#     file = open(f"./image/{i}.jpg", "wb")
#     # for chunk in response:
#     #     file.write(chunk)
#     # f.close()
#     file.write(response.content)
    
#     file.close()

# response = requests.get(img_link[0])
# file = open("./image/sample_image.jpg", "wb")
# file.write(response.content)
# file.close()


# with open("imagelink.txt", 'w') as file:
#    links = file.read().splitlines()
# for link in img_link:
#     response = requests.get(link,  headers=headers1)
#     print(response.status_code)





# broken_images = []
# for i,img in enumerate(img_link[::-1]):
#     print(type(img))
#     # We can split the file based upon / and extract the last split within the python list below:
#     file_name = f"./image/{i}.jpg"
#     print(f"This is the file name: {file_name}")
    # Now let's send a request to the image URL:

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'

headers3 = { 'User-Agent' : user_agent }

r = requests.get("https://n2k3y9s6.stackpathcdn.com/wp-content/uploads/2021/12/header800x400-min-100x70.png", headers=headers1)
# We can check that the status code is 200 before doing anything else:
print(r.status_code)
# if r.status_code == 200:
#     # This command below will allow us to write the data to a file as binary:
#     with open(f"./image/kk.jpg", 'wb') as f:
#         for chunk in r:
            # f.write(chunk)
        
