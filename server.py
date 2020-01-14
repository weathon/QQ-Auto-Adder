from colorama import Fore,Back,Style
import datetime
import http.server

print("This version is a beta version, if you find some bugs, please report to us.")
print(Fore.YELLOW+"Warning: http.server is not recommended for production. It only implements basic security checks.")
print (Style.RESET_ALL)

unittest=False

if unittest:
    with open(input("Drop your file here")) as f:
        myfile=f.read()
    qqids=myfile.split("\n")
else:
    qqids=["1","2","3","4","5"]

total=len(qqids)
index=0

print("Finished loading files, please start your Android device/emulator and connect.")

for i in qqids:
    print("Waiting for next add")
    print(Fore.MAGENTA+"["+str(datetime.datetime.now())+"]\n"+"Adding "+i+Fore.RESET)
    try:
        #code start here

        #end of main code
        index+=1
        print(str(index)+" added, "+str(total)+" left")
    except:
        print("Error during adding "+i)
    print()
