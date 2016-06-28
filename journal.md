NEXT
  - goal: _maybe_ figure out matplotlib
  - definitely figure out how to sample
  - 💚http://willdrevo.com/fingerprinting-and-audio-recognition-with-python/
    - https://github.com/worldveil/dejavu/blob/master/dejavu/wavio.py
  - maybe http://stackoverflow.com/questions/2648151/python-frequency-detection
  - http://stackoverflow.com/questions/4431481/frequency-detection-from-a-sound-file
  - http://stackoverflow.com/questions/23377665/python-scipy-fft-wav-files
  - http://glowingpython.blogspot.com/2011/08/how-to-plot-frequency-spectrum-with.html

2016-07-28

- GOAL: by the end of the night:
  - have all .mp3 files saved as .wav files (probably via ffmpeg)
  - have at least some kind of matplotlib visualization of the tracks
- Ran `brew install ffmpeg` to get that loaded
- Found http://superuser.com/questions/675342/convert-mp3-to-wav-using-ffmpeg-for-vbr for ideas of how to convert
- Created a tmp directory so I could play around with it and copied an mp3 in there
- Ran `ffmpeg -i cello_A2_15_pianissimo_arco-normal.{mp3,wav}` and it worked!
- ffmpeg can only take 1 argument at a time as far as I can tell, so write a python script to convert them all
  - http://stackoverflow.com/questions/89228/calling-an-external-command-in-python
    ```python
    from subprocess import call
    call(["ls", "-l"])
    ```
- Googled for these:
  - http://stackoverflow.com/questions/4450592/string-interpolation-in-python
  - http://www.stealthcopter.com/blog/2009/09/python-making-multi-depth-directories/
  - ended up with `convert.py` serially but it was super slow
  - that was super slow, so worked out a faster method
  - http://stackoverflow.com/questions/31344582/python-multiprocessing-cpu-count-returns-1-on-4-core-nvidia-jetson-tk1
  - http://stackoverflow.com/questions/7207309/python-how-can-i-run-python-functions-in-parallel
  - Got final version that ran much faster
    - n cores `python convert.py  218.73s user 152.09s system 599% cpu 1:01.90 total`
    - n * 1.5 cores `python convert.py  215.86s user 147.26s system 637% cpu 56.998 total`
    - n * 2 cores ``
  - http://stackoverflow.com/questions/814167/easiest-way-to-rm-rf-in-python
  - wrote some slow code to download everything
    - `python download.py  4.41s user 4.20s system 5% cpu 2:25.57 total`
  - rewrote it to use threads
    - `python download.py  5.51s user 6.18s system 16% cpu 1:10.71 total`

- Tried to make http://samcarcagno.altervista.org/blog/basic-sound-processing-python/ work
  - Got really stuck because I just have one channel
  - http://stackoverflow.com/questions/23154400/read-the-data-of-a-single-channel-from-a-stereo-wave-file-in-python
  - Took me 2+ hours to realize that I was being too clever, and just copy-pasting from the original worked fine
  - Couldn't get Matplotlib to work

- Got this email from Keith:
  ```
  This is a very interesting project!

  Yes, your next big challenge is representation of the clips J … once you get over that hurdle - my guess is breaking the frequency ranges up and producing some density measurement of frequencies and mapping them into a vector would be a place to start, but that’s my 10 seconds of thinking about it … there may be easier methods.   Either way, you’ll be well on your way to training that NN.

  If you’ve not used Python much, I’d highly recommend the PyCharm IDE by Jetbrains.  The FREE community edition is about as good as it gets … unless you want to use Jupyter Notebooks and make your exploration a bit more interactive.  I am a big fan of reducing the learning curve and PyCharm brings a lot to the table for someone just learning the language.

  I’ve got a really decent NN video series I can share with you … first (its been a while), so I’ve got to find it (on YT) … I think you’d really find it useful and like the presentation of material (I did).  I think he even has code to play with.

  https://www.youtube.com/watch?v=pHMzNW8Agq4 (This is kind of the middle of a series, but a good place to get warmed up to what you’re about to do).

  Also, this book is an oldie but goodie and probably the most comprehensive “foundational” book on computer science out there … I had recently thought of taking my favorites out of this book and doing them in Python since this book has a C and Pascal version only.  This one is near and dear to my heart and while finding a hard copy is not hard (and not expensive if you do), I once owned 2 copies … only have 1 now.  I like the Pascal version, but the C version is probably worthwhile.

  You will find the treatment of induction, recurrence relations, and Big O analysis thorough (if not mathematically rigorous).

  https://www.amazon.com/Foundations-Computer-Science-Principles/dp/0716782847/ref=pd_cp_14_2?ie=UTF8&refRID=KQT1T171RFZEHEKCBMPE

  The FREE version is online at Stanford :

  http://infolab.stanford.edu/~ullman/focs.html

  Enjoy!
  K:M
  ```

2016-07-26

- Downloaded all sounds from non-percussion of http://www.philharmonia.co.uk/explore/make_music/violin
  - Unzipped and added to the `./sounds` directory
- Googled "python list directory"
  - http://stackoverflow.com/questions/3207219/how-to-list-all-files-of-a-directory-in-python
  - Copy / pasted and tweaked
- Had to search "python substring"
  - http://stackoverflow.com/questions/663171/is-there-a-way-to-substring-a-string-in-python
- Has to google "python dictionaries" to figure out
  ```python
    key = string.replace(dirpath, path + '/', '')
    if len(key) > 1:
        if not sounds.has_key(key):
            sounds[key] = []
        sounds[key].extend(filenames)
  ```
- Had to google all kinds of things
  - how to import files
  - how to glob
  - how to map / reduce

2016-07-24

- Took https://www.khanacademy.org/math/calculus-home

Before 2016-07-24

Googled a _lot_ and found all of these resources:

- http://neuralnetworksanddeeplearning.com/chap1.html
- http://natureofcode.com/book/chapter-10-neural-networks/
- https://processing.org/tutorials/sound/
- http://www.philharmonia.co.uk/explore/make_music/cello (music clips)
- http://zulko.github.io/blog/2013/10/04/read-and-write-audio-files-in-python-using-ffmpeg/
- http://bastibe.de/2012-11-02-real-time-signal-processing-in-python.html
- https://github.com/idiap/bob
- http://www.kdnuggets.com/2015/06/top-20-python-machine-learning-open-source-projects.html
- http://dsp.stackexchange.com/questions/17682/how-do-i-construct-input-to-neural-network-from-audio-signals
- https://m.reddit.com/r/MachineLearning/comments/2inwyk/audio_processing_by_neural_network/
- http://benanne.github.io/2014/08/05/spotify-cnns.html
- https://www.coursera.org/course/audio
- http://samcarcagno.altervista.org/blog/basic-sound-processing-python/
- http://dsp.stackexchange.com/questions/2610/scipy-audio-processing
- (I should BUY) https://www.packtpub.com/big-data-and-business-intelligence/building-machine-learning-systems-python
- http://jack.minardi.org/software/computational-synesthesia/
- http://willdrevo.com/fingerprinting-and-audio-recognition-with-python/
- http://colah.github.io/posts/2014-07-Conv-Nets-Modular/
