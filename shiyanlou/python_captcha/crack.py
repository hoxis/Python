# --coding:utf8--
from PIL import Image

image = Image.open('45.png')

# 将图片转换为8位像素模式
image.convert('P')

# 打印颜色直方图
print(image.histogram())

his = image.histogram()
values = {}

for i in range(256):
    values[i] = his[i]

for j,k in sorted(values.items(), key=lambda x:x[1], reverse=True)[:10]:
    print(j, k)