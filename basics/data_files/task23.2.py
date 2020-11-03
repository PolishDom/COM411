def search(filepath):
  print("Searching...")

  with open(filepath) as file: 
    for line in file:
      print(f"Looked in {line}")
    
    print ("...Done!")

def run():
  location = search("basics/data_files/locations.txt")

run()
