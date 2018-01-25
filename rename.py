# Get all files from the directory
# For each file rename

import os
print(os.getcwd())
os.chdir (r"C:\Users\zotech_pc\Downloads\prank\prank")
lists = os.listdir(r"C:\Users\zotech_pc\Downloads\prank\prank")
print(lists)
def renameFile():
    for eachFile in lists:
        os.rename(eachFile, eachFile.strip("0123456789"))
       
renameFile()
print (lists)
