# --coding:utf8--
from qcloud_image import Client
from qcloud_image import CIUrl, CIFile, CIBuffer, CIUrls, CIFiles, CIBuffers
appid = '1254259578'
secret_id = 'AKID5GH7nMzkcKtHTTq2c1FIAtUxFdLvraif'
secret_key = 'vfQ3VL3Zu42qTJzWJD2xyIk28MPI2sZ7'
bucket = 'blog'
client = Client(appid, secret_id, secret_key, bucket)
client.use_http()
client.set_timeout(30)

print (client.porn_detect(CIFiles(['./45.png',])))