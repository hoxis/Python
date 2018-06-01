import argparse

from PIL import Image

# 命令行输入参数处理
parser = argparse.ArgumentParser()

parser.add_argument('file', help='the input file')     # 输入图片
parser.add_argument('-o', '--output', help='the output text file')   # 输出文件
parser.add_argument('-w', '--width', type=int, default=40,
                    help='the width of the output, default is 40')    # 输出字符画宽度
parser.add_argument('--height', type=int, default=40,
                    help='the height of the output, default is 40')   # 输出字符画高度

# 获取参数
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

ascii_char = list(
    "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# 将256 灰度映射到 70 个字符上


def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return " "
    length = len(ascii_char)
    gray = int(0.2126*r + 0.7152*g + 0.0722*b)

    # 每个字符对应的 gray 值区间宽度
    unit = (256.0+1)/length

    # gray值对应到 char_string 中的位置（索引值）
    index = int(gray/unit)
    return ascii_char[index]


if __name__ == "__main__":

    im = Image.open(IMG)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'

    print(txt)

    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        with open('output.txt', 'w') as f:
            f.write(txt)
