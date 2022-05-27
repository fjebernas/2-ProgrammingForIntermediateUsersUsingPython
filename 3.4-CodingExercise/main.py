
f = open("textFile.txt","w")
f.write("Python is simpler")

f = open("textFile.txt","a")
f.write("\nFurther improve my programming skills")
f.write("\nBy experimenting and making more programs")
f.write("\nTo be a legit software engineer!")

f = open("textFile.txt","r")
print(f.read())

f.close()