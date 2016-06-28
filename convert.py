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

def convert_paths(paths):
    for path in paths:
        new_path = string.replace(path, './sounds/', './wav/')
        new_path = string.replace(new_path, '.mp3', '.wav')
        mkdir_p(new_path)
        call(["ffmpeg", "-i", path, new_path, "-y"])

def convert_in_parallel():
    paths = glob.glob('./sounds/**/*.mp3')
    chunks = chunk(paths, cpu_count() * 2)
    processes = []
    for list in chunks:
        process = Process(target=convert_paths, args=(list,))
        process.start()
        processes.append(process)

    for process in processes: process.join()
    print "All done!"

if __name__ == '__main__':
    convert_in_parallel()
