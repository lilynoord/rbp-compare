import tkinter as tk
from Comparers import *
from Parsers import *
from FileSelect import *
parsedRBPGlobal = dict
def openDataWindow(parsedSeqs,parsedRBP):
    global parsedRBPGlobal
    parsedRBPGlobal = parsedRBP
    saveAll()
    """global parsedSeqsGlobal, parsedRBPGlobal
    parsedRBPGlobal = parsedRBP
    parsedSeqsGlobal = parsedSeqs
    dataWindow = tk.Tk()
    dataWindow.title('Analyze Data')
    dataWindow.wm_minsize(300,400)
    #TODO: save all functionality
    global saveAll
    saveAllButton = tk.Button(dataWindow,text="Save all comparisons to single file",command=saveAll)
    saveAllButton.pack() 
    geneList = tk.Listbox(dataWindow)
    geneList.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
    scrollbar = tk.Scrollbar(dataWindow)
    scrollbar.pack(side=tk.RIGHT,fill=tk.BOTH)
    for gene in parsedRBP:
        geneList.insert(tk.END,gene)

    geneList.config(yscrollcommand = scrollbar.set)
    scrollbar.config(command = geneList.yview)
    geneList.bind('<<ListboxSelect>>', onselect)


    dataWindow.mainloop()"""
    

def analyzeGene(gene:str,rbp:dict):
    
    return compareHandler(gene,rbp,False)

def saveAll():
    print("SAVE ALL")
    filename = save_file()
    print("\n\n\n")
    print("FileName:",filename.name)
    f = open(filename.name, "a")
    for i in parsedRBPGlobal:
        if i != "Prediction Info":
            f.write(analyzeGene(i,parsedRBPGlobal))
    f.close()
    return

def onselect(evt):
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    index = int(w.curselection()[0])
    gene = w.get(index)
    print(compareHandler(gene,parsedRBPGlobal,False))


"""x,y = parserHandler("C:/Users/Lily/Desktop/RBPcompare/files/testlist.txt","C:/Users/Lily/Desktop/RBPcompare/files/All_Predictions.txt","_ref","_alt")
openDataWindow(x,y)"""