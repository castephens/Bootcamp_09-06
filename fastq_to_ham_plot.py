# Import a FASTQ file, calculate the hamming distances for each sequence,
# and plot these distances in a way you think is useful.

# Script must ultimately be contained in one fluid .py file merged via GitHub

import matplotlib.pyplot as plt

file = "CTGATC.fastq"

def getSeqs(fastq_file):
    #Parse a FASTQ for sequence identities and corresponding sequences
    sequences = {}
    count = 1
    with open(fastq_file, 'r') as f:
        for line in f:
            line = line.rstrip('\n')
            if "@" not in line and "<" not in line and "#" not in line and "+" not in line:
                sequences[count] = line
                count += 1
            
    return(sequences)

def hamDist(str1, str2):
   #Count the # of differences between equal length strings str1 and str2
    str1list = list(str1)
    str2list = list(str2)
    diff = 0
    for i in range(1,len(str1list)+1):
        if str1list[i-1] == str2list[i-1]:    
            continue
        else:
            diff+=1
    
    return(diff)

sequences = getSeqs(file)
all_diffs = []
#for i in range(1,len(sequences.keys())+1):
for i in range(1,500):
        print(sequences[i] )
        seq1 = sequences[i] 
        #for j in range(1,len(sequences.keys())+1):
        for j in range(1,500):
            if i != j and j < len(sequences.keys()):
                seq2 = sequences[j+1]
                if len(seq1) == len(seq2):
                    all_diffs.append(hamDist(seq1,seq2))

print(len(all_diffs))           

#Make some kind of plot that contains the data you've calculated.
#plt.show()