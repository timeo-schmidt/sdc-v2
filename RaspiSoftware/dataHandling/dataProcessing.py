"""

Convert Folder To a single CSV File. This is not done on the vehicle
    - Time left estimator
    - finished file size estimator

    // Idea: Load datapoints in chunks into memory
            Then flush/append into csv
"""


import os
import numpy as np
import pickle

dataFolder = "DEVtrainingData/2018-04-20 17:39:25.751708/"
outputFileName = "csvOutput"


# for root, dirs, files in os.walk("../", topdown=False):
#    for name in files:
#       print(os.path.join(root, name))
#    for name in dirs:
#       print(os.path.join(root, name))
#

def convertFile2csv(fileName, csvPath):
    #open dumped Pickle
    f = pickle.load( open( (dataFolder+fileName), "rb" ) )
    path = csvPath + outputFileName
    print(path)
    np.savetxt(path, f, delimiter=",", newline="", fmt="%d", footer="\n")
    with open(path, "a") as a:
        a.write("LOL")
    print("One File Written.")


def mergeDir2csv(inputPath, outputPath=""):
    # Walk Through Pickle Files
    for _,_,files in os.walk(inputPath):
        for file in files:
            convertFile2csv(file, outputPath)



mergeDir2csv(dataFolder)
