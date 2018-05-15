#-*-coding:utf-8 -*-
import sys
import datetime
import time

class Log:
  def __init__(self, filename,ncols,Qtime,dic,count,):
    self.filename = filename
    self.ncols = ncols
    self.Qtime = Qtime
    self.dic=dic
    self.count=count
  def parse(self):
    i=1
    #f=file(self.filename)
    import linecache
    file = open(self.filename, 'r')
    linecount = len(file.readlines())
    # print linecount
    CurrentTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 获取当前时间
    # print(CurrentTime)
    timeArray = time.strptime(str(CurrentTime), "%Y-%m-%d %H:%M:%S")
    print(timeArray)
    timeStamp = int(time.mktime(timeArray)) - self.Qtime - 28800 #要取该时间日志的时间(当前时间的前多少秒)
    print(timeStamp)
    # print self.Qtime
    while True:
      #line=f.readline()
      line=linecache.getline(self.filename,linecount)
      linecount = linecount - 1
      if len(line)==0:
        break
      ip=line.split('|')
      time1 = ip[0].split(' ')
      datetimeObj1 = datetime.datetime.strptime(time1[0], "%d/%b/%Y:%H:%M:%S") #把10/Nov/2017:16:58:44这个格式的时间转为 2017-11-14 16:25:39
      timeArray = time.strptime(str(datetimeObj1), "%Y-%m-%d %H:%M:%S")
      LogTime = int(time.mktime(timeArray))#把时间转为时间戳
      if LogTime > timeStamp:
        if ip[self.ncols] in self.dic:
          self.dic[ip[self.ncols]]=self.dic[ip[self.ncols]]+1
        else:
          self.dic[ip[self.ncols]]=i
      else:
        break
    soredic=sorted(self.dic.items(), key=lambda d:d[1],reverse=True)
    counts=0;
    ipList = []
    for item in soredic:
      if counts==int(self.count):
        break
      if item[1] > 50:
        # print("IP:%s  Total Times: %s"%(item[0],item[1]))
        ipList.append(item[0])
      counts=counts+1
    # print ipList
    file.close()
    return ipList
if __name__=="__main__":
  pass
  #if len(sys.argv) < 3:
    #print('usage:log.py log.log toptimes\nexample log.py log.log 20\ncode by iswin')
    #sys.exit()
  dic={}
  log = Log('access.log',1,8110000,dic,5)
  # log = Log('/root/PycharmProjects/python_atuo/iptables/sztcpc.log',1,36000,dic,5)
  # log.parse()
  # log=Log(sys.argv[1],dic,sys.argv[2])
  log.parse()
