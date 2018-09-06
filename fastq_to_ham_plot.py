# Import a FASTQ file, calculate the hamming distances for each sequence,
# and plot these distances in a way you think is useful.

# Script must ultimately be contained in one fluid .py file merged via GitHub

import matplotlib.pyplot as plt

f = open(CTGATC.fastq)

def getSeqs(fastq_file):
	#Parse a FASTQ for sequence identities and corresponding sequences
	seqences = {}
	return sequences

def hamDist(str1, str2):
   #Count the # of differences between equal length strings str1 and str
   str1list = list(str1)
   str2list = list(str2)
   diff = 0
   for i in range(1,len(str1list)+1):
       if str1list[i]i == str2list[i]:
           continue
       else:
           diff += 1
   return diff

#Make some kind of plot that contains the data you've calculated.
sequences = getSeqs(f)
total_diff = []
for index, string in sequences.items():
    for place, seq in sequences.items():                         
        if place  == index:
            continue
        if len(string) != len(seq):
            continue
        else:
            count_dif = hamDist(string,seq)
            total_diff.append(count_dif)

