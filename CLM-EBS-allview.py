import time
import datetime
import linecache

#get time
timeStr=time.strftime("%Y%m%d",time.localtime(time.time()))
timeNow=str(bytes(int(time.time())))
#longTime=time.mktime(datetime.datetime.now().timetuple())
print timeStr,timeNow 
#,longTime

#read file
#file_from=open("/var/ftp/pub/ebs/remote/ebsebsCapacity_"+timeStr+".txt")
fileName="/var/all_view/ebs/remote/ebsCapacity_"+timeStr+".txt"
#print fileName
try:
   txt=linecache.getline(fileName,2)
except IOError:
   print "Error: Read failed"
else:
   print "Successfully read"
#print txt
result=txt.split(",")
#print result[1],result[2]

#write file
disk_total=str(bytes(int(long(result[1])/1024/1024/1024)))
disk_allocation=str(bytes(int(long(result[2])/1024/1024/1024)))
outStr="{\"start_time\":"+timeNow+",\"stop_time\":"+timeNow+",\"resource_id\":\"CPC-RP-SH-01\",\"resource_type\":\"blockstorage\",\"disk_total\":"+disk_total+",\"disk_allocation\":"+disk_allocation+"}"
#print outStr
ouputFileName="/var/all_view/sh/summary/poolsummary.log."+time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
#print ouputFileName
try:
  output=open(ouputFileName,'w')
  output.write(outStr)
except IOError:
   print "Error: Write failed"
else:
   print "Successfully write"
   output.close()
print "success"