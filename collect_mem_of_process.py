# -*- coding: utf-8 -*-
'''
Created on 2017年3月26日

@author: sunjiali
'''
#!/usr/bin/env python
from subprocess import Popen,PIPE
import os
def getPid(process_name):
    
    p = Popen(['pidof',process_name],stdout=PIPE,stderr=PIPE)
    pids = p.stdout.read().split()
    
    return pids

def parsePidFile(pids):
    sum = 0
    for i in pids:
        fn = os.path.join('/proc/',i,'status')
        with open(fn) as fd:
            for line in fd:
                if line.startswith('VmRSS'):
                    mem = int(line.split()[1])
                    sum += mem
                    break
    return sum

def total_mem(f):
    with open(f) as fd:
        for line in fd:
            if line.startswith('MemTotal'):
                total_mem = int(line.split()[1])
                return total_mem
if __name__ == '__main__':
    
    process_name = 'java'
    pids = getPid(process_name)
    mem = parsePidFile(pids)
    total_mem = total_mem('/proc/meminfo')
    
    print process_name + "'s memory is: %sKB" % mem
    
    print "Percent %.2f%%" % (mem/float(total_mem)*100) + " of total"
    
    
    
                    
    
        
    