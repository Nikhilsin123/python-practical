from collections import counter
def word_count(fname):
  with open(fname) as f:
    return counter(f.read().split())
  print("number of word in the file",word_count("test.txt"))
