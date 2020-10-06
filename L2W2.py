first_number = input("Input first number?")
second_number = input("Input second number?")

if (first_number > second_number):
    print("First is bigger!")
elif (first_number < second_number):
    print("First is smaller!")    
else:
    print("Both are equal!")

print("Done!")

print("I am going to check your entity")

entity = input("what entity are you? Human, Robot, Animal")

if (entity == "Human" or "human"):
  print("you are a human")

elif (entity == "Robot"):
  print("you are a robot")

elif (entity == "Animal"):
  print("you are an Animal")

else:
  print("I do not know what you are!")

print ("Complete")