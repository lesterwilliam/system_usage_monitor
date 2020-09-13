#
from __future__ import print_function
import psutil
import sys

print('cpu_percent:\t', psutil.cpu_percent(interval=1), '%')
print('memory_used:\t', psutil.virtual_memory()[2], '%')
print('cpu_count:\t\t', psutil.cpu_count(logical=False), 'cores')
print('cpu_freq:\t\t', psutil.cpu_freq())
print('disk_usage C:\t', psutil.disk_usage('C:/')[3], '%')
print('disk_usage D:\t', psutil.disk_usage('D:/')[3], '%')
