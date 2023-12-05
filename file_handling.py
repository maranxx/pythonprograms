# F1 = open("file1.txt", "r")       (# r= read only, can create file in this mode)  (w=write only,can create file in this mode) # (a=append only,can create file in this mode)
                                    # (r+ = read & write,cannot create file in this mode) (w+ =read and write) # (a+ = read and append)
# data = F1.read()                  (# x = used to create a file)
# print(data)

F1 = open("file1.txt", "w")
F1.write("again it is rick grimes")

F1 = open("file1.txt", "r+")

print(F1.read())
print(F1.tell())
F1.write(" hi maran")
print(F1.tell())
