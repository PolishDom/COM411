#We can write to a file by opening a file in write mode and using the method write.

with open("output.txt", "w") as file:
  file.write("some text")

#We can also write out multiple lines using the method writelines which takes a list as an argument. Note, that each line in the list will need to include the end of line character.
lines = ["first line\n", "second line\n"]
with open("output.txt", "w") as file:
  file.writelines(lines)