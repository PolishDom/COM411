def search(nameofafile):
  print("Searching...")
  sections = []
  books = []
  with open(nameofafile) as file:
    for line in file:
      if line str.startswith("Section"):
        sectionsplit = str.split(":")
        sections.append(sectionsplit[1])
      
      else:
        books.append(line)

  print("Done!")
  sections_and_books = (sections[],books[])
  return sections_and_books

def save(nameofafile,storedtuple):
  print ("Saving...")
  with open("section-books.txt", "w") as file:
    file.write(f"Sections: {sections}")
    file.write(f"Books: {books}}")
  print ("Done!")

def run():
  data = search("basics/data_files/books.txt")
  data2 = save("basics/data_files/section-books.txt")

run()