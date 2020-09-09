#
from __future__ import print_function
import psutil
print(psutil.cpu_percent())
print(psutil.virtual_memory())
print('memory % used:', psutil.virtual_memory()[2])
print(psutil.cpu_count())
print(psutil.cpu_freq())
print(psutil.cpu_stats())
print(psutil.disk_usage('C:/'))
print(psutil.disk_usage('E:/'))