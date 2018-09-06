# Import a FASTQ file, calculate the hamming distances for each sequence,
# and plot these distances in a way you think is useful.

# Script must ultimately be contained in one fluid .py file merged via GitHub

import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

#Variables
xHammDist = 0 #All the hamming distances
yFreq = 0 #Number of times each hamming distance repeats itself

#f = open(CTGATC.fastq)

def getSeqs(fastq_file):
	#Parse a FASTQ for sequence identities and corresponding sequences
	seqences = {}
	return sequences

def hamDist(str1, str2):
   #Count the # of differences between equal length strings str1 and str2
   diffs = 0
   return diffs

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


hamm_dist =[1,2,3,4,5,6,7,8,9,13,12,14,15,16,13,1,2,3,4,5,6,7,8,1,3,12,12,7,9,8,8,7,9,4,5,6,8,7,6,3,6,4,5,8,12,20]


plotHistogram(hamm_dist)
