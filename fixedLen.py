#simple program for opening a text file and adding whitespace such that 
#each line has the same length
#useful for parsing data and seeking to a specific line

import os 
print(os.getcwd()) #print out the file location
os.chdir(input("directory: ") #change the file location to the target folder
print(os.getcwd()) #print out the new file location

fil = input("File name: ")
raw = open(fil + '.txt','r') #open the file
         
file = [n.strip() for n in raw.readlines()] #strip off tabs from the front and back
maxLen = max([len(n) for n in file]) #determine the maximum length of lines
print(maxLen)

output = open(fil +'Rect.txt','w') #create a new file for the edited data
for i in file: output.write("%-*s \n" % (maxLen,i)) #write the file

output.close() #close the opened files
raw.close()
