 def observed():
  observations = []
  for objects in range(7):
    observation = input("Please enter an observation: ")
    observations.append(observation)
  return observations

def run():
  print ("counting observations...")
  observations = observed()
  whatdidtheysee_set = set()
  for observation in observations:
    whatdidtheysee_set.add((observation, observations.count(observation)))
  print (whatdidtheysee_set)

run()










list.count 