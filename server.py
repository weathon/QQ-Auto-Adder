from colorama import Fore,Back,Style
import datetime
import web

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
indexnum=-1
print("Finished loading files, please start your Android device/emulator and connect.")


class index:
    def GET(self):
        global indexnum
        try:
            if indexnum>=total:
                print("Finish!")
                input()
            print(str(indexnum)+" added, "+str(total)+" total.")
            print(Fore.MAGENTA+"["+str(datetime.datetime.now())+"]\n"+"Adding "+str(qqids[indexnum])+Fore.RESET)
            indexnum+=1
            print()
            return qqids[indexnum]
        except:
            print(Fore.RED+"Error during adding "+qqids[indexnum]+Fore.RESET)
        

if __name__ == "__main__":
    app = web.application(("/","index"), globals())
    app.run()


