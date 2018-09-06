# Import a FASTQ file, calculate the hamming distances for each sequence,
# and plot these distances in a way you think is useful.

# Script must ultimately be contained in one fluid .py file merged via GitHub

import matplotlib.pyplot as plt
from collections import Counter
import numpy as np


file = "CTGATC.fastq"

#Variables
xHammDist = 0 #All the hamming distances
yFreq = 0 #Number of times each hamming distance repeats itself



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
hamm_dist = []
#for i in range(1,len(sequences.keys())+1):
for i in range(1,500):
        print(sequences[i] )
        seq1 = sequences[i] 
        #for j in range(1,len(sequences.keys())+1):
        for j in range(1,500):
            if i != j and j < len(sequences.keys()):
                seq2 = sequences[j+1]
                if len(seq1) == len(seq2):
                    hamm_dist.append(hamDist(seq1,seq2))         

#Make some kind of plot that contains the data you've calculated.

def countHamm(hamm_dist):
    """ Counts number of times each Hamming distance appears by using Counter and dictionary, and makes x list (xHammDist) and y list (yOcurrences), returns these values"""
    HammDic= {}
    HammDic = Counter(hamm_dist)
    xHammDist = HammDic.keys()
    yFreq = HammDic.values()
    print(HammDic)
    print(xHammDist)
    print(yFreq)
    return xHammDist, yFreq

def plotHamm(xHammDist, yFreq):
    """Plot the x y coordinates and title Hamming Distance Frequency"""
    plt.plot(xHammDist, yFreq)
    plt.title('Hamming Distance Frequency')
    #plt.axis()
    plt.grid(True)
    plt.ylabel('Frequency')
    plt.xlabel('Hamming Distance')
    plt.show()

def plotHistogram(hamm_dist):
    mean = np.mean(hamm_dist)
    stdev = np.std(hamm_dist)
    histHamm = plt.hist(hamm_dist, 50, density = True, facecolor ='g')
    plt.xlabel('Hamming distance')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.title('Hamming Distance Frequencies')
    meanStdev = r'$\mu=$' + str(mean)
    plt.text(60, 0.025, r'$\mu=$'+ str(mean) + r'$\sigma=$' + str(stdev))
    plt.show()

plotHistogram(hamm_dist)

