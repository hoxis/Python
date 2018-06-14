# coding=utf-8
#! python3

import requests, os, bs4, threading

url = 'http://xkcd.com/'
os.makedirs("xkcd2", exist_ok=True)

def downloadXkcd(start,end):
    for urlNum in range(start, end):

        print("Downloading page http://xkcd.com/%s ..." % urlNum)
        response = requests.get(url + str(urlNum))
        print("the return code : " + str(response.status_code))

        soup = bs4.BeautifulSoup(response.text, "html.parser")
        comic = soup.select('#comic img') #获取id属性为comic内的img元素
        if comic == []:
            print('cannot get the comic image')
        else:
            imageUrl = url + (comic[0].get('src'))
            print("downing the image %s..." %imageUrl)
            response = requests.get(imageUrl)
            print("the return code : " + str(response.status_code))

            # download the image
            print(os.path.basename(imageUrl))
            
            #  save the image to ./xkcd
            image = open(os.path.join('xkcd', os.path.basename(imageUrl)), 'wb')
            for i in response.iter_content(1000):
                image.write(i)
            image.close()

downloadThreads = []

for i in range(1, 101, 10):
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i+9))
    downloadThreads.append(downloadThread)
    downloadThread.start()

for downloadThread in downloadThreads:
    downloadThread.join()

print('Done.')
