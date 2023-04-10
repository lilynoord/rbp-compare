from tkinter import filedialog as fd
import tkinter as tk
from Pairwise import *
#TODO: compare proteins between alleles within a gene

def compareHandler(gene:str,rbp:dict,newWin:bool):
    """
    Compare the RBPs for a specific gene. 
    """
    if newWin:
        #compareGeneNewWin(gene,seq,rbp)
        print("Currently there is no functionality for displaying RBPcompare info in a new window")
    else:
        return compareGeneNoWin(gene,rbp)
    return
    

def compareGeneNoWin(gene,rbp):
    """
    Compare a single gene's RBPs without opening a new window. Returns a string containing the comparison data.
    """
    
    refRBPs = rbp[gene]["Ref"]
    altRBPs = rbp[gene]["Alt"]
    output = ""
    gainedStr = ""
    lostStr = ""
    gained = 0
    lost = 0
    for i in altRBPs: 
        if i not in refRBPs:
            gainedStr += str(i) + "\t"
            for pos in range(1,len(altRBPs[i])):
                gainedStr += str(altRBPs[i][pos][0]) + " "
            gainedStr += "\n"
            gained += 1
    for i in refRBPs: 
        if i not in altRBPs:
            lostStr += str(i) + "\t"
            for pos in range(1,len(refRBPs[i])):
                lostStr += str(refRBPs[i][pos][0]) + " "
            lostStr += "\n"
            lost += 1
    gained = str(gained)
    lost = str(lost)
    output += "Gene:\t" + gene + "\n" + "Total Gained:\t" + gained + "\n" + "Total Lost:\t" + lost + "\n"
    output += "\nRBPs Gained:\nName\tPositions\n" + gainedStr + "\nRBPs Lost:\nName\tPositions\n" + lostStr + "\n\n\n"
    return output
def compareGeneNewWin(gene,seq,rbp):
    """
    Non-functional
    """
    geneWindow = tk.Tk()
    geneWindow.title(gene)
    geneWindow.wm_minsize(400,200)
    refSeq = seq[gene]["Ref"]
    altSeq = seq[gene]["Alt"]
    diffs = pairwise(gene,seq)[0]
    refBp = tk.Label(geneWindow,text=refSeq)
    refBp.grid(row=10,column=3)
    altBp = tk.Label(geneWindow,text=altSeq)
    altBp.grid(row=12,column=3)
    match = ""
    print(diffs)
    for i in range(0,len(altSeq)):
        if i == diffs:
            match = match + "X"
        else:
            match = match + "_"
    matchBp = tk.Label(geneWindow,text=match)
    matchBp.grid(row=11,column=3)
    geneWindow.mainloop()
    return 
