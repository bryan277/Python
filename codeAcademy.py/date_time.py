from datetime import datetime

now = datetime.now()
print(now)
# 2018-06-12 11:20:41.843289

current_year = now.year
current_month = now.month
current_day = now.day

print(current_day)
#12
print(current_month)
#6
print(current_year)
#2018

print('%02d-%02d-%04d' % (now.month, now.day, now.year))
# 06-12-2018

print(now.hour)
print(now.minute)
print(now.second)
# 11
# 40
# 7

print('%02d:%02d:%02d' % (now.hour, now.minute, now.second))
# 11:44:12

print ('%02d/%02d/%04d %02d:%02d:%02d' % (now.month, now.day, now.year, now.hour, now.minute, now.second))
#06/12/2018 11:48:34
