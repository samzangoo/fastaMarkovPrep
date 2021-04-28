"""
CS123B Final Project Coding
Author: Sam Zangooie
"""
# Importing random function and SeqIO from biopython
# If biopython is not installed use the command "pip install biopython"
import random
from Bio import SeqIO

# User input to determine the dataset filename
filename = input("Enter dataset filename: ")

# Using biopython to parse the fasta file and save as a list of SeqIO formatted sequences
fullSet = list(SeqIO.parse(filename, "fasta"))
fullSize = len(fullSet)

# Setting up some variables which we'll use to determine set sizes down the line
basicSize = fullSize/2
relatedSize = basicSize
# Setting up arrays which we'll populate using our fullSet
fullSetFasta = []
basicSet = []
relatedSet = []
i = 0

# Populating arrays
for unit in fullSet:
    fullSetFasta.append(unit.format("fasta"))
    if i < basicSize:
        basicSet.append(unit)
        i += 1
    else:
        relatedSet.append(unit)

# To make things easier on ourselves, we make new arrays for our sets in fasta format
fastaBasicSet = []
for unit in basicSet:
    fastaBasicSet.append(unit.format("fasta"))

fastaRelatedSet = []
for unit in relatedSet:
    fastaRelatedSet.append(unit.format("fasta"))

# Opening up our first files for our basic and related sets
basicSetFile = open('basic_set.fasta', 'w')
relatedSetFile = open('related_set.fasta', 'w')

# Writing to our new files based on our basic and related sets
for unit in fastaBasicSet:
    basicSetFile.write(unit)
    basicSetFile.write("\n")

for unit in fastaRelatedSet:
    relatedSetFile.write(unit)
    relatedSetFile.write("\n")

# Opening files and arrays for writing our basic training and testing fasta files.
basicTrainingFile = open('basic_training.fasta', 'w')
basicTraining = []
basicTestingFile = open('basic_testing.fasta', 'w')
basicTesting = []

# We make a variable to represent the 80% size of our training sets
basicTrainingSize = round(basicSize * 0.8)
i = 0

# Writing to test/training files and appending arrays in fasta format
for unit in fastaBasicSet:
    if i < basicTrainingSize:
        basicTraining.append(unit)
        basicTrainingFile.write(unit)
        basicTrainingFile.write("\n")
        i += 1;
    else:
        basicTesting.append(unit)
        basicTestingFile.write(unit)
        basicTestingFile.write("\n")


# Opening files and arrays for writing our related training and testing fasta files.
relatedTrainingFile = open('related_training.fasta', 'w')
relatedTraining = []
relatedTestingFile = open('related_testing.fasta', 'w')
relatedTesting = []
i = 0

# Writing to test/training files and appending arrays in fasta format
for unit in fastaRelatedSet:
    if i < basicTrainingSize:
        relatedTraining.append(unit)
        relatedTrainingFile.write(unit)
        relatedTrainingFile.write("\n")
        i += 1
    else:
        relatedTesting.append(unit)
        relatedTestingFile.write(unit)
        relatedTestingFile.write("\n")

# We use the imported random function to shuffle our list of sequences for
# the creation of our random set.
shuffleSequence = fullSetFasta
random.shuffle(shuffleSequence)

randomSet = []
i = 0

# Allocating the first half of the newly shuffled set to be our random set.
for unit in shuffleSequence:
    if i < basicSize:
        randomSet.append(unit)
        i += 1

# Opening and writing a file for our entire random set.
randomSetFile = open('random_set.fasta', 'w')

# Writing the random set to our randomSet file
for unit in randomSet:
    randomSetFile.write(unit)
    randomSetFile.write("\n")

# Opening files for writing our random training and testing fasta files.
randomTrainingFile = open('random_training.fasta', 'w')
randomTraining = []
randomTestingFile = open('random_testing.fasta', 'w')
randomTesting = []
i = 0

# Allocating units to training and testing sets based on pre-established format.
for unit in randomSet:
    if i < basicTrainingSize:
        randomTraining.append(unit)
        randomTrainingFile.write(unit)
        randomTrainingFile.write("\n")
        i += 1
    else:
        randomTesting.append(unit)
        randomTestingFile.write(unit)
        randomTestingFile.write("\n")

print("All datasets have been successfully created.")
