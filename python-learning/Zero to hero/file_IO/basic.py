# The key function for working with files in Python is the open() function.

# The open() function takes two parameters; open(filename,mode)

# There are four different methods (modes) for opening a file:


# "r" - Read - Default value. Opens a file for reading,
# error if the file does not exist

# "a" - Append - Opens a file for appending,
# creates the file if it does not exist

# "w" - Write - Opens a file for writing, 
# creates the file if it does not exist

# "x" - Create - Creates the specified file, 
# returns an error if the file exists

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)


f = open("apna collage/file_IO/example.txt","r")
readFulltext = f.read()
f.close

f = open("apna collage/file_IO/example.txt","r")
readOneLine = f.readline()
f.close

f = open("apna collage/file_IO/example.txt","w")
readOneLine = f.write("i am sexy buddhadeb")
f.close

f = open("apna collage/file_IO/example.txt","a")
readOneLine = f.write("\ndebesh is sexy boy")
f.close

# different way to write same things -->

with open("apna collage/file_IO/example.txt","r") as l:
    data = l.read()
    print(data)
    # here dont need to close the open file
    
#  delete file 

#first need to import a os module 
# import os

# os.remove("apna collage/file_IO/example.txt")


# to remove folder -->
# os.rmdir("myfolder") # replace with folder path (myfolder)