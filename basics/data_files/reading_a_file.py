#reading a file
file = open("data.txt")

#closing a file
file.close()

#with to automatically close a file
with open("data.txt") as file:
  # do something with the file

#reading as a string using read
with open("data.txt") as file:
  data = file.read()
  lines = data.split('\n')

#read only a few characters
with open("data.txt") as file:
  partial_data = file.read(10)

#retrieve all lines ina file as list using readlines command
with open("data.txt") as file:
  lines = file.readlines()

#reading a single line using readlines
with open("data.txt") as file:
  line = file.readline().strip()

#loop through file line by line 
with open("data.txt") as file:
  for line in file:
    # do something with the line from the file
    # line.strip() will remove any white space including the \n character