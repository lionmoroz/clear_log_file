import os
import sys
import shutil
## The script created  for cleaning and copying log file when their size more as {log_critical_size}

log_name = sys.argv[1] #name the log file
log_critical_size = int(sys.argv[2]) # critical size of log file in kB
log_number = int(sys.argv[3])# how much times copy previous log file


if len(sys.argv) < 4:
    print("Mising arguments") 

def log_clear (log_name, log_critical_size , log_number):
    if os.path.isfile(log_name):# check if file exist
        log_file_size = os.stat(log_name).st_size # check file size
        log_file_size = log_file_size // 1024 # set kB size

        if log_file_size >= log_critical_size:
            if log_number > 0:
                for file_number in range(log_number, 1, -1):
                    src = log_name + "_" + str(file_number-1)
                    dst = log_name + "_" + str(file_number)

                    if os.path.isfile(src):
                        shutil.copyfile(src,dst)
                        print(f"File {src} copied to {dst}")

                shutil.copyfile(log_name, log_name + '_1')
                print(f"Copied {log_name} to {log_name + '_1'}")
            else:
                print("You set argument log number 0")
            myfile = open(log_name,'w')
            myfile.close()

        else:
            print("Your file size isn`t larger than the critical size ")
    else:
        print("Please, check directory, i can`t to search this file")

        
log_clear(log_name, log_critical_size, log_number)