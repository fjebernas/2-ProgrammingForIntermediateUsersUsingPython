import os

# f = open("textFile.txt","w")
# f.write("Python is simpler")

# f = open("textFile.txt","a")
# f.write("\nFurther improve my programming skills")
# f.write("\nBy experimenting and making more programs")
# f.write("\nTo be a legit software engineer!")

# f = open("textFile.txt","r")
# print(f.read())

# f.close()

# f = open("textFile.txt")

# print(f.read())
# print(f.readline())
# for x in f:
#     print(x)

# f.close()

if os.path.exists("textFile.txt"):
    os.remove("textFile.txt")
else:
    print("This file doesn't exist anymore")