from os import listdir
from os.path import isfile, join
files = [f for f in listdir('c:/') if isfile(join('c:/', f))]
print(files)