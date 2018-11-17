import urllib.request
import re
import string
import random
f = open('imagenet.synset.txt')
size=6
chars=string.ascii_uppercase + string.digits
products=[]
line = f.readline()
while line:
  imagename=''.join(random.choice(chars) for _ in range(size))+'.jpg'
  urllib.request.urlretrieve(line,imagename)
  line = f.readline()
f.close()