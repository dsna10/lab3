#!/usr/bin/env python3
'''Lab 3 Part 4 script - subprocess'''
# Author ID: [seneca_id]

import subprocess

def free_space():
    process = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", 
                               stdout=subprocess.PIPE, 
                               shell=True)
    output = process.communicate()[0].decode('utf-8').strip()
    return output

if __name__ == '__main__':
    print(free_space())
