print ("Program Started! ")
#Since ascii is a number I need to change it into an integer
asci = int(input("Please enter a ascii code "))

print (asci)

#If VARIABLE in RANGE(0,100)
# {} .format the format bit will put inside the brackets
#chr goes from integer to letter in ascii
if asci in range(32,126):
  print ("The ascii number for ", asci , "the letter is {}".format(chr(asci)))

else:
  print ("Wrong number fool")

print ("End of program")