import os,shutil

try:
    for root,sufolders,filenames in os.walk('/'):
        for name in filenames:
            filepath = os.path.join(root, name)
            if os.path.getsize(filepath)/1024/1024 > 100:
                print(filepath)
                print(os.path.getsize(filepath)/1024/1024)
except:
    #print('An exception happened: ' + str(err))
    print()
    #raise err
