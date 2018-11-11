import datetime
"""
timestamps = ['2010-01-12', '2011-01-12, 2009-02-12']
dates = [datetime.datetime.strptime(ts, "%Y-%m-%d") for ts in timestamps]
dates.sort()
sorteddates = [datetime.datetime.strftime(ts, "%Y-%m-%d") for ts in dates]
sorteddates
"""

import time
timestamps = ['01 Mar 2017', '03 Feb 2117', '15 Jan 1998', '28 Dec 1993']
timestamps.sort(key=lambda x: time.mktime(time.strptime(x,"%d %b %Y")))
print(timestamps)