from os import walk
import glob

def add_to_result(path):
    parts = path.split("/")[3].split("_")
    return {
        'path': path,
        'instrument': parts[0],
        'note': parts[1],
        'length': parts[2],
        'volume': parts[3],
        'filename': parts[4],
    }

def get_sounds():
    paths = glob.glob('./sounds/**/*.mp3')
    return map(add_to_result, paths)
