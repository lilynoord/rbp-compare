import tkinter as tk
from FileSelect import *
from Parsers import *
from ErrorHandler import *
from DataAnalyzer import *
#Global Variables
seqs = "None Selected"
rbp = "None Selected"
refSuffix = "_ref"
altSuffix = "_alt"


#Function handlers - call functions in other files and handle the outputs. Makes buttons easier to work with, theoretically...

def selectAllSequenceFiles():
    global seqs
    seqs = str(select_file("Sequence File"))
    updateFileNames()
def selectRBPmapFile():
    global rbp
    rbp = str(select_file("RBPmap File"))
    print(rbp)
    updateFileNames()
comparePackage = 0
def runComparison():
    if (rbp =="None Selected"):
        tk.messagebox.showerror(title="File Error",message="Please select a file")
        return
    refSuffix = refSuffixEntry.get()
    altSuffix = altSuffixEntry.get()
    global parsedSeqs
    global parsedRBP
    parsedSeqs,parsedRBP = parserHandler(seqs,rbp,refSuffix,altSuffix)
    #print("Done!")
    warnError()
    openDataWindow(parsedSeqs,parsedRBP)





# Main Window function
mainWindow = tk.Tk()
mainWindow.title('RBP Compare')
mainWindow.geometry('300x320')  
mainFrame = tk.Frame(mainWindow)
mainFrame.pack()
topFrame = tk.LabelFrame(mainFrame,text="Select files for comparison")
topFrame.pack(expand=True)
openAllSequencesFileButton = tk.Button( topFrame,text='Select Sequences File',command=selectAllSequenceFiles,state="disabled")

openAllSequencesFileButton.pack(expand=True) 

openRBPmapFileButton = tk.Button(topFrame,text='Select RBPmap File',command=selectRBPmapFile)
openRBPmapFileButton.pack(expand=True)

bottomFrame = tk.LabelFrame(mainFrame)
bottomFrame.pack(expand=True)
file1 = tk.Label(bottomFrame,text="Sequences file: " + seqs)
file1.pack()
file2 = tk.Label(bottomFrame,text="RBPmap file: " + rbp)
file2.pack()

runCompare = tk.Button(bottomFrame,text="Run Comparison",command=runComparison)

runCompare.pack(expand=True)

footerFrame = tk.LabelFrame(mainFrame,text="Allele Suffixes")
footerFrame.pack()

refSuffixEntry = tk.Entry(footerFrame)
refSuffixEntry.insert(0,refSuffix)
refSuffixEntry.pack()
altSuffixEntry=tk.Entry(footerFrame)
altSuffixEntry.insert(0,altSuffix)
altSuffixEntry.pack()

clearLogButton = tk.Button(mainWindow,text="Clear Error Log",command=clearErrorLog)
clearLogButton.pack()




def updateFileNames():
    print(seqs,rbp)
    file1["text"] = "Sequences file: " + str(seqs)
    file2["text"] = "RBPmap file: " + str(rbp)
    file1.update()
    file2.update()


mainWindow.mainloop()