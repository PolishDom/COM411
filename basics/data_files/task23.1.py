import os

def cwd():
  filepath = os.getcwd()
  print(f"Current Working Folder Path: {filepath}")
  for cwdfile in os.listdir(filepath):
    print(cwdfile)

def run():
  print ("Processing...")
  filecwd = cwd()

run()
