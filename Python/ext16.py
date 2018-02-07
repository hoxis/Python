# -- coding:utf-8 --
from sys import argv

script, filename = argv

print "We're going to erase %r." %filename
print "If you don't want that, hit CTRL-C(^C)."
print "If you do want that,hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
#target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I'm going to write these to file."

target.write(line1 + "\n" + line2 + "\n" + line3)
# 相当于为每个line执行write，不会追加新行，需要手动\n
# target.writelines([line1,line2,line3])

target = open(filename)

print "Print the file: ", filename
print target.read()

print "And finally, wo close it."
target.close()