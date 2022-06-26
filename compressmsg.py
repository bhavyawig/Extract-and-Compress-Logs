import os 
import shutil 
from os import path 


#log = open("/var/log/syslog") 


filebanao = open("messages.txt","w+") # to create a message.txt file 

with open("/var/log/syslog") as log:  # to have all contents of var/log/syslog in log variable 
            for i in log:             # to have a for loop in the log variable 
                  filebanao.write(i)  # to write to the file created as the file was formed in w+ ->write mode 



src = path.realpath("messages.txt") # src stores the path of messages.txt
root_dir,tail = path.split(src)     # this separates the name of the file from the path ( 2 parts : name of the file, rest of the path without name)
shutil.make_archive("messages.txt","zip",root_dir)  # to make a zip file  , make_archive (file to be ziped, format of new file, path of the new file)
filebanao.close() # close the message.txt file 

 
