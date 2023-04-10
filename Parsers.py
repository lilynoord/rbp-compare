from ErrorHandler import *

class PredictionInfo:
    def __init__(self,info):
        self.info = info

# 
def parserHandler(seqs,rbp,refSuffix,altSuffix):
    """Master handler function for both comparisons"""
    parsedSeqs = dict # parseSeqs(seqs,refSuffix,altSuffix)
    parsedRBP = parseRBP(rbp,refSuffix,altSuffix)
    return parsedSeqs, parsedRBP




def parseRBP(rbp:str,refSuffix:str,altSuffix:str):
    """
    Parses and breaks down the rbp file. 
        Arguments:
            `rbp:str` File path for RBP file.
            `refSuffix:str` suffix indicating reference allele.
            `altSuffix:str` suffix indicating altered allele.
        Suffixes are set in the main menu. Default is _ref and _alt
    
    """
    file = open(rbp,"r")
    file = file.read()
    file = file.split("*")
    predictionInfo = PredictionInfo(file[0])
    comparedGenes = {"Prediction Info":predictionInfo}
    length = len(file)
    
    
    for i in range(1,length):
        alleleName = ""
        
        element = file[i]
        nSplit = element.split("\n")

        if nSplit != [''] and nSplit != ['','']:
            if nSplit[2] != "":
                alleleName = nSplit[2]
                

                eqSplit = element.split("==============================================================================")
                alleleDict = {}
                for protein in range(1,len(eqSplit)):
                    proteinSplit = eqSplit[protein].split("\n\nProtein: ")
                    for protein in proteinSplit:
                        proteinList = []
                        protein = protein.split("\n")
                        proteinName = protein[0]
                        proteinList.append(proteinName)
                        for line in range(2,len(protein)):
                            proteinLineSplit = protein[line].split()
                            if proteinLineSplit != []:
                                proteinList.append(proteinLineSplit)
                        if proteinName != "":
                            alleleDict[proteinName] = proteinList
                
                geneName, refOrAlt = handleAlleleName(alleleName,refSuffix,altSuffix)
                if geneName not in comparedGenes:
                    comparedGenes[geneName] = {}
                comparedGenes[geneName][refOrAlt] = alleleDict
    
    """for gene in comparedGenes: 
        #print("Gene:", gene)
        for allele in comparedGenes[gene]:
            print(allele)
            for protein in comparedGenes[gene][allele]:
                print(protein, str(len(comparedGenes[gene][allele][protein])-1))
            print("")
    """
    
    
    return comparedGenes

def handleAlleleName(alleleName:str,refSuffix:str,altSuffix:str):
    """
    Determines what the gene name is and whether or not the given allele is a ref or alt sequence, using the input suffixes.
    """
    if refSuffix in alleleName:
        use = refSuffix
        refOrAlt = "Ref"
    elif altSuffix in alleleName:
        use = altSuffix
        refOrAlt = "Alt"
    else:
        logError("'" + alleleName + "' Does not contain ref/alt suffixes: " + refSuffix +"/"+ altSuffix)
        use=""
        refOrAlt="REF/ALT UNKNOWN"

    geneName = alleleName.replace(use,"")
    return geneName, refOrAlt


#breakdownRBP("C:/Users/Lily/Desktop/RBPcompare/files/All_Predictions.txt","_ref","_alt")




def parseSeqs(seqs,refSuffix,altSuffix):
    "Parses the sequences, returns a `seqDict` object."
    seqDict = {}
    file = open(seqs,"r")
    file = file.read()
    file = file.split(">")

    for i in file:
        if i != "":
            i = i.split("\n")
            geneName, refOrAlt = handleAlleleName(i[0],refSuffix,altSuffix)
            if geneName not in seqDict:
                    seqDict[geneName] = {}
            seqDict[geneName][refOrAlt] = i[1]


    """  for each in seqDict:
        for i in seqDict[each]:
            print(each,i,seqDict[each][i])
            print()
        print()
        print()"""
    return seqDict



