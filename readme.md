# RBP_compare


## **User Manual**

## Main Menu

---

Assumption here is that the alleles for each gene are labeled with the name of the gene and then a ref/alt suffix. 
For example, the CD7 gene has a ref/alt pair labeled: 
`'CD7_alt` and `CD7_ref`. If you have a different suffix, please be sure to change it in the main menu before running the comparison.

Currently sequence-analysis is non-functional, this app only compares the RBPmap data.

## **Code Documentation**

## Classes

---

### **PredictionInfo**

#### Variables:

    predictionsForJob:str
    calculationParameters:str
    genome:str
    selectedMotifs:str
    stringencyLevel:str
    conservationFilter:str


## Important Data Structures/Variables

---

### **`comparedGenes`**

`comparedGenes` is a dictionary that holds all the allele pairs that have had their RBP map data compared. 

    comparedGenes = {
        "Prediction Info": PredictionInfo,
        "Gene 1": <geneDict>,
        "Gene 2": <geneDict>,
        ...
    }


### **`geneDict`**
`geneDict` is the specific formatting for each gene's RBP comparison data within `comparedAlleles`. Formatted as follows:

    geneDict =  {
        "refAllele": <alleleDict>,
        "altAllele": <alleleDict>
    }

### **`alleleDict`**
`alleleDict` is the specific formatting for each allele's RBP comparison data within a `geneDict`. 

    alleleDict = {
        "protein 1": <proteinList>,
        "protein 2": <proteinList>,
         ...
    }

### **`proteinList`**
`proteinList` is an array containing the data for a given RBP calculated for the allele. 

    proteinList = [
    0:  "name", 
    1:  [position 1],
    2:  [position 2],
    3:  [position 3],
    ...
    ]

The position data for the protein is stored as another list with the following structure: 

    [
    0: Sequence Position,
    1: motif,
    2: K-mer,
    3: Z-score,
    4: P-value
    ]



### **`seqDict`**
`seqDict` is a dictionary holding the seq data for each gene. Not currently used.

    seqDict = {
        "gene":<alleleSeqDict>,
        "gene":<alleleSeqDict>,
        ...
    }

### **`alleleSeqDict`**
`alleleSeqDict` is a dictionary holding the sequence data for each gene. It holds both the sequences and the mutation location data. These are designed with solitary point mutations in mind, but should be able to handle multiple mutations within a single gene. Not currently used.

    alleleSeqDict = {
        "Ref" : "Sequence",
        "Alt" : "Sequence",
    }



# Split method for compareRBP:
```
1: Split by "**********************************************"
2: parse 1st item into `PredictionInfo`
3: for each item from 2nd:
    1: split by "=============================================================================="
    2: iterate through first item:
        1: split lines
        2: discard first line
        3: grab name from 2nd line
            1: search for ref/alt suffix
            2: record name + ref/alt
            3: add item to proper gene object.
    3: Split by "\nProtein: "
    2: for each item: 
        1: Split lines
        2: for each line:
            1: Grab protein name from first line
            2: Discard 2nd line
            3: for each line from 3:
                1: split by " "
                2: for each item: 
                    1: Save first item to sequnce position
                    2: save second item to motif
                    3: save third item to Z-score
                    4: save fourth item to P-Value

```
# Split method for compareSeqs:
Not currently used.
```
1: Split by ">"
2: for each: 
    1: split line
    2: for first line: 
        1: search for ref/alt suffix
        2: record name + ref/alt
        3: add item to proper gene object.
    3: for second line 

```


