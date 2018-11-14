# This program sorts the dates from oldest to newest


import datetime

import time
timestamps = ['01 Mar 2017', '03 Feb 2117', '15 Jan 1998', '28 Dec 1993']
timestamps.sort(key=lambda x: time.mktime(time.strptime(x,"%d %b %Y")))
print(timestamps)
