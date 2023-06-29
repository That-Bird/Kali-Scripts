#!/usr/bin/env python3

import shutil
import psutil

## Let's first define a check_disk_usage function that will receive a distant check and Returns positive if disk usage is under 80%
def check_disk_usage(disk):
    ##Create a named tuple ‘du’ containing the total, current, and free disk space on the directory passed as an argument into the ‘check_disk_space’ function
    du = shutil.disk_usage(disk)
    ##Create variable ‘free’ set equal to the percentage of total disk space still free
    free = du.free / du.total * 100
    ##Return a boolean (positive if >20% of disk space free, negative otherwise
    return free > 20

## Write another function called check_cpu_usage. In this case, we'll check the usage for a whole second. We'll say the machine is healthy if cpu_usage is less than 75 percent.
def check_cpu_usage():
   ##Create variable usage and set equal to the percentage of max CPU processing used in past 1 second
    usage = psutil.cpu_percent(interval=1)
   ##Return a boolean (positive if CPU usage <75%, negative otherwise)
    return usage < 75

##Prints “ERROR” if either of the functions return negative, otherwise prints “Everything is ok!”
if not check_disk_usage('/') or not check_cpu_usage():
    print("error")
else:
    print("everything is ok")

##Two lines that print the current CPU usage percentage (last 1 second and the percentage of disk space used in the PC
##Passing ‘/’ as an argument into shutil.disk_usage() references the root directory, which contains all of the files on the virtual machine
print("CPU Usage:",psutil.cpu_percent(interval=1),"%")
print("Disk Usage:",round((100-(shutil.disk_usage('/').free / shutil.disk_usage('/').total * 100)),2),"%")

