import os

file_path = '/users/ayomideadeyina/Downloads/Ayomide_Adeyina,_MS_-_Software_Engineer (1).pdf'

print(file_path)

if os.path.isfile(file_path):
    os.remove(file_path)
    print("File has successfully been deleted")
else:
    print("This file does not exist!")