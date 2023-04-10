import datetime
import tkinter as tk
errorCount = 0

def logError(msg):
    global errorCount
    errorCount += 1
    f = open("./files/errorlog.txt", "a")
    f.write("\n"+str(datetime.datetime.now())+": " + str(msg))
    f.close()
    
def warnError():
    if errorCount > 0:
        tk.messagebox.showwarning(title="Warning",message="Warning: " + str(errorCount) + " errors occurred while parsing the selected files. This may or may not impact the analysis of the data. See the error logs for details.")
def warning(mssg:str):
    tk.messagebox.showwarning(title="Warning",message="Warning: " + mssg)
def clearErrorLog():
    open('./errorlog.txt', 'w').close()
