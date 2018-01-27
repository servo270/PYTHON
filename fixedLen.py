import os #handy library for interacting with files
import random
print(os.getcwd()) #print out the file location
os.chdir('files') #change the file location to the 'files' folder
print(os.getcwd()) #print out the new file location

fil = input("File name: ")
raw = open(fil + '.txt','r')
file = [n.strip() for n in raw.readlines()]
maxLen = max([len(n) for n in file])
print(maxLen)
output = open(fil +'Rect.txt','w')
for i in file: output.write("%-*s \n" % (maxLen,i))
output.close()
