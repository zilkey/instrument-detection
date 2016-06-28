import os
from multiprocessing import Process, cpu_count
import glob
from subprocess import call
import string
from utils import mkdir_p, chunk

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
