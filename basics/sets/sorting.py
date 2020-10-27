def observed():
  observations = []
  for objects in range(5):
    observation = input("Please enter an observation: ")
    observations.append(observation)
  return observations

def remove_observations(removal):
  removalquestion = "yes"
  while removalquestion == "yes":
    removalquestion = input("Would you like to remove an observation?  yes/no ")
    if removalquestion == "yes":
      whatobservation = input("Which observation would you like to remove? ")
      removal.remove(whatobservation)
      print ("Done! You have removed an observation")

    elif removalquestion == "no":
      print ("Done!")

    else:
      print("You inputted it wrong")
    
  return removal

def run():
  print ("counting observations...")
  observations = observed()
  removing = remove_observations(observations)
  whatdidtheysee_set = set()
  for observation in observations:
    whatdidtheysee_set.add((observation, observations.count(observation)))
  print (whatdidtheysee_set)


run()