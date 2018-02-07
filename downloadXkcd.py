# --coding=utf-8--
#! python3

import requests, os, bs4

url = 'http://xkcd.com/5/'
os.makedirs("xkcd", exist_ok=True)

while not url.endswith('#'):
    #  download the page
    print("Downloading page %s ..." % url)
    response = requests.get(url)
    print("the return code : " + str(response.status_code))

    soup = bs4.BeautifulSoup(response.text, "lxml")

#    tmpFile = open("xkcd.tmp", 'wb')
#    for tmp in response.iter_content(1000):
#        tmpFile.write(tmp)

    #  find the url of the comic image
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

    # get the prev button'url
    prev = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prev.get('href')

print('Done.')
