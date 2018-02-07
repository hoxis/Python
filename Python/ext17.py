# --coding:utf-8--
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "copying from %s to %s" %(from_file, to_file)

in_file = open(from_file)
indata = in_file.read()

print "###the input file is %s bytes long" %len(indata)
print "###the input file is:\n %s" %indata

print "does the output file exists? %s" %exists(to_file)
print "ready, hit Return to continue, Ctrl-C to abort."
raw_input("> ")

out_file = open(to_file,'w+')
out_file.write(indata)

# out_file.seek(0)
# print "the output file is:\n %s" %out_file.read()
print "Alright, all done."

out_file.close()
in_file.close()

out_file = open(to_file)
print "the output file is:\n %s" %out_file.read()

out_file.close()