import os
"""Write a Python program to list only directories, files and all directories, files in a specified path."""

spec_path = r'C:\Users\Ruslan\Desktop\NI Multisim'
dirs_only = []
files_only = []
for i in os.listdir(spec_path):
    if os.path.isdir(os.path.join(spec_path,i)):
        dirs_only.append(i)
    else:
        files_only.append(i)
print(dirs_only)
print(files_only)

"""Write a Python program to check for access to a specified path. 
Test the existence, readability, writability and executability of the specified path"""

spec_path2 = r'C:\Users\Ruslan\Desktop\NI Multisim'

print(os.access(spec_path2,os.W_OK))
print(os.access(spec_path2,os.F_OK))
print(os.access(spec_path2,os.R_OK))
print(os.access(spec_path2,os.X_OK))

"""Write a Python program to test whether a given path exists or not. 
If the path exist find the filename and directory portion of the given path."""

spec_path3 = r'C:\Users\Ruslan\Desktop\NI Multisim'

if os.path.exists(spec_path3):
    print(os.path.dirname(spec_path3))
    print(os.path.basename(spec_path3))

"""Write a Python program to count the number of lines in a text file."""

with open(r'C:\Users\Ruslan\Desktop\rand\random.txt','r') as f:
    print(len(f.readlines()))

"""Write a Python program to write a list to a file."""

with open(r'C:\Users\Ruslan\Desktop\rand\random.txt','a') as f:
    l = ['hello','its me','I was wondering','if after all these years',"you'd like to meet"]
    f.write('\n'+str(l))

"""Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt"""

path = r"C:\Users\Ruslan\Desktop\rand"
for i in range(26):
    with open(path + '\\' + chr(i+65)+'.txt','w'):
        pass

"""Write a Python program to copy the contents of a file to another file"""

with open(r'C:\Users\Ruslan\Desktop\rand\random.txt','r') as f:
    contents = f.read()
    with open(r'C:\Users\Ruslan\Desktop\rand\randomcopy.txt','w') as c:
        c.write(contents)

"""Write a Python program to delete file by specified path. 
Before deleting check for access and whether a given path exists or not."""

spec_path4 = r'C:\Users\Ruslan\Desktop\rand\del.txt'

if os.path.exists(spec_path4):
    os.remove(spec_path4)