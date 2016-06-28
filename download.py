from threading import Thread
from StringIO import StringIO
from zipfile import ZipFile
from urllib import urlopen
import shutil
import string
import os
from utils import mkdir_p, chunk

urls = [
    'http://www.philharmonia.co.uk/assets/audio/samples/banjo/banjo.zip',
    'http://www.philharmonia.co.uk/assets/audio/samples/bass%20clarinet/bass%20clarinet.zip',
    'http://www.philharmonia.co.uk/assets/audio/samples/bassoon/bassoon.zip',
    'http://www.philharmonia.co.uk/assets/audio/samples/cello/cello.zip',
    'http://www.philharmonia.co.uk/assets/audio/samples/clarinet/clarinet.zip',
    'http://www.philharmonia.co.uk/assets/audio/samples/contrabassoon/contrabassoon.zip',
    'http://www.philharmonia.co.uk/assets/audio/samples/cor%20anglais/cor%20anglais.zip',
    'http://www.philharmonia.co.uk/assets/audio/samples/double%20bass/double%20bass.zip',
    'http://www.philharmonia.co.uk/assets/audio/samples/flute/flute.zip',
    'http://www.philharmonia.co.uk/assets/audio/samples/french%20horn/french%20horn.zip',
    'http://www.philharmonia.co.uk/assets/audio/samples/guitar/guitar.zip',
    'http://www.philharmonia.co.uk/assets/audio/samples/mandolin/mandolin.zip',
    'http://www.philharmonia.co.uk/assets/audio/samples/oboe/oboe.zip',
    'http://www.philharmonia.co.uk/assets/audio/samples/saxophone/saxophone.zip',
    'http://www.philharmonia.co.uk/assets/audio/samples/trombone/trombone.zip',
    'http://www.philharmonia.co.uk/assets/audio/samples/trumpet/trumpet.zip',
    'http://www.philharmonia.co.uk/assets/audio/samples/tuba/tuba.zip',
    'http://www.philharmonia.co.uk/assets/audio/samples/viola/viola.zip',
    'http://www.philharmonia.co.uk/assets/audio/samples/violin/violin.zip',
]

# http://stackoverflow.com/questions/5710867/python-downloading-and-unzipping-a-zip-file-without-writing-to-disk
def download_and_unzip(url, sounds_path):
    response = urlopen(url)
    zipdata = StringIO()
    zipdata.write(response.read())
    zip = ZipFile(zipdata)
    parts = url.split("/")
    folder_name = parts[len(parts) - 2]
    for name in zip.namelist():
        uncompressed = zip.read(name)
        outputFilename = sounds_path + '/' + folder_name + '/' + name
        mkdir_p(outputFilename)
        print "Saving extracted file to ",outputFilename
        output = open(outputFilename,'wb')
        output.write(uncompressed)
        output.close()

def download_in_serial():
    sounds_path = "./sounds/mp3"
    wav_path = "./sounds/wav"

    if os.path.exists(sounds_path): shutil.rmtree(sounds_path)
    if os.path.exists(wav_path): shutil.rmtree(wav_path)

    threads = []
    for url in urls:
        download_and_unzip(url, sounds_path)

def download_in_parallel():
    sounds_path = "./sounds/mp3"
    wav_path = "./sounds/wav"

    if os.path.exists(sounds_path): shutil.rmtree(sounds_path)
    if os.path.exists(wav_path): shutil.rmtree(wav_path)

    threads = []
    for url in urls:
        thread = Thread(target=download_and_unzip, args=(url, sounds_path,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    download_in_serial()
