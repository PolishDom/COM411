#We can read a file by simply providing the file name of the file we wish to read to the function open:
file = open("data.txt")

#It is important to close a file once we are done processing it so as to free it for use by other processes.  We can do this simply by using the method close:
file.close()

#In order to ensure that a file is closed once we are done processing it, we can use the keyword with:

with open("data.txt") as file:
  # do something with the file

#We can read the entire content of the file using the method read.

with open("data.txt") as file:
  data = file.read()

#We can also read only a few characters by supplying an appropriate value to the method read:
with open("data.txt") as file:
  partial_data = file.read(10)

#It is often useful to retrieve all the lines in a file as list using the method readlines, read a single line using the method readline or loop through the file line by line:
with open("data.txt") as file:
  for line in file:
    # do something with the line from the file