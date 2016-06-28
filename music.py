import sound_list
from pylab import*
from scipy.io import wavfile

# Taken from http://samcarcagno.altervista.org/blog/basic-sound-processing-python/
# print sound_list.get_sounds()

def create_samples(path):
    sampFreq = 44110
    sampFreq, snd = wavfile.read(two_channel)
    snd = snd / (2.**15)
    s1 = snd[:,0]
    timeArray = arange(0, 5060.0, 1)
    timeArray = timeArray / sampFreq
    timeArray = timeArray * 1000
    plot(timeArray, s1, color='k')
    ylabel('Amplitude')
    xlabel('Time (ms)')

two_channel = '/Users/galvanize/Downloads/440_sine.wav'
one_channel = './tmp/cello_A2_15_pianissimo_arco-normal.wav'

# create_samples(two_channel)
create_samples(one_channel)
