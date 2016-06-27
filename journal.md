2016-07-24

- Took https://www.khanacademy.org/math/calculus-home

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
