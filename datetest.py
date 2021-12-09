from datetime import datetime

todaystr = '2021-11-11'
todaydt = datetime.strptime(todaystr,'%Y-%m-%d')
print(todaydt.timestamp())
todayint = int(todaydt.timestamp())
todaystr2 = datetime.strftime(datetime.fromtimestamp(todayint),'%Y-%m-%d')
print(todaystr2)

