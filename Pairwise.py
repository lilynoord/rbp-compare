from ErrorHandler import *
def pairwise(gene:str,seqs:str):
    refSeq = seqs[gene]["Ref"]
    altSeq = seqs[gene]["Alt"]
    diffs = []
    if(len(refSeq) == len(altSeq)):
        for i in range(0,len(altSeq)):
            print(i,refSeq[i],altSeq[i])
            if refSeq[i] != altSeq[i]:
                print("MISMATCH")
                diffs.append(i)
        return diffs
        
    else:
        warning("There is currently no functionality for comparing sequences of different lengths")
        