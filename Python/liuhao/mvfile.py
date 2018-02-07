import os, re, shutil

filereg = re.compile(r'(.jpg|.pdf)$')
for foldername, subfolders, filenames in os.walk('.'):
    print('The current folder is: ' + foldername)
    print('Subfolders: ',end="")
    print(subfolders)
#    print('The file in current folder: ', end="")
    #print(filenames)
    for filename in filenames:
       if filereg.search(filename) != None:
           print(os.getcwd())
           print(filename)
           shutil.move(filename, '/mnt/e/liuhao_data/OneDrive/code/Python/')
