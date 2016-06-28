import os
from multiprocessing import Process, cpu_count
import glob
from subprocess import call
import string

def mkdir_p(filename):
	folder=os.path.dirname(filename)
	if not os.path.exists(folder):
		os.makedirs(folder)

def chunk(list, size):
    i = 0
    j = 0
    result = []
    for x in range(0,size): result.append([])
    for item in list:
        result[j].append(item)
        i += 1
        if j == size - 1: j = 0
        else: j += 1
    return result
