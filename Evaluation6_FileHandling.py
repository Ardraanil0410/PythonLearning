import os
with open("myfile.txt","w") as file:
    file.write("Ardra Latheesh Tanvi")

with open("myfile.txt","r") as file:
    content=file.read()
    print(content)

file_path="myfile.txt"
os.remove(file_path)
print("File deleted ")
