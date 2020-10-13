#Instead of doing this everytime we can do it in a function
print("Please enter your name")
name = input()
print("Hello", name)



# This is the function we can make this into
def greet_user():
  print("Please enter your name")
  name1 = input()
  print("Hello", name1)


#then we just recall the function
greet_user()
