def search(nameofafile):
  print("Searching...")
  sections = []
  books = []
  with open(nameofafile) as file:

    for line in file:

      if line.startswith("Section"):
        part = line.split(":")
        sections.append(part[1][:-1])
      else:
        books.append(line[:-1])

  print("Done!")
  sections_and_books = (sections,books)
  return sections_and_books


def save(nameofafile,storedtuple):
  print ("Saving...")

  with open(nameofafile , "w") as file:
    file.write("Sections: ")
    for element in storedtuple[0]:
      file.write(element + " , ")

    file.write("\n Books: ")
    for element in storedtuple[1]:
      file.write(element + " , ")

  print ("Done!")

def run():
  data = search("basics/data_files/books.txt")
  data2 = save("basics/data_files/section-books.txt",data)

run()


