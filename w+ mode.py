  # in write + or w+ mode we can create a new file or it will override the existing file after reading the  file
  # point the file pointer towards the starting

file1 = open("file2.txt", "w+")
print(file1.tell())
file1.write("hi i am the real nigga")
print(file1.tell())
file1.seek(0)
print(file1.tell())
data = file1.read()
print(data)
