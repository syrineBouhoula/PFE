#!/usr/bin/env python$
#coding:utf-8$

#Import the library.$
import os
import subprocess
import psutil

filename="ResourseUsage.csv"
#csv = open(filename, 'w')	
#csv.write("Ram_usage,CPU_usage\n")
#csv.close

x=1
while True:
 try:
  # Getting % usage of virtual_memory ( 3rd field)
  ram=psutil.virtual_memory()[2]
  print('RAM memory used:', psutil.virtual_memory()[2],'%')

  # Calling psutil.cpu_precent() for 4 seconds
  cpu=psutil.cpu_percent(4)
  print('The CPU usage is: ', psutil.cpu_percent(4),'%')
  csv = open(filename, 'a')
  csv.write(str(ram)+ "%" + ",")
  csv.write(str(cpu)+ "%" +"\n")
  csv.close()
  
 except RuntimeError as error:
 # Errors happen fairly often, DHT's are hard to read, just             >
        print(error.args[0])
        time.sleep(2.0)
        continue

