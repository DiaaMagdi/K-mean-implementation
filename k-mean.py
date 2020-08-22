# -*- coding: utf-8 -*-
"""
Created on Sat May  4 20:18:07 2019

@author: Light
"""

import pandas as pd
import random

#taking input of k and the rows or data i'll work on
Trainingdf = pd.read_excel("./TrainingData.xlsx")
k = 3   #TODO input k and columns to apply classification on

#assigning initial random rows to the centroids
rowSet = set()
for i in range(Trainingdf.shape[0]):
    rowSet.add(i)


centroidsDataFrame = []
for i in range(k):
    centroidsDataFrame.append(pd.DataFrame())
    
rndm = -1
for i in range(Trainingdf.shape[0]):
    while not(rndm in rowSet):
        rndm = random.randint(0, Trainingdf.shape[0])
    rowSet.remove(rndm)
    centroidsDataFrame[i%k] = centroidsDataFrame[i%k].append(Trainingdf.iloc[rndm])
del i, rndm, rowSet

#calculating the means of the centroids dataframes
means = []
for i in centroidsDataFrame:
    means.append(round(i.mean(), 3))
del i
#constructing the main loop
while True:
    #deleteing the rows in the dataframes
    for i in range(k):
        centroidsDataFrame[i] = centroidsDataFrame[i].drop(centroidsDataFrame[i].index, axis=0)
    del i
    
    for xi in range(Trainingdf.shape[0]):
        x = Trainingdf.iloc[xi]
        
        #calculating distances from x
        distances = []
        for i in range(len(means)):
            distances.append(0)
            for j in Trainingdf.columns:
                distances[i] += round(abs(means[i][j] - x[j]), 3)
        del i, j
        
        #getting the minimum of the distance to assign the x to it's centroid
        minValue = distances[0]
        minIndex = 0
        for i in range(len(distances)):
            if(minValue > distances[i]):
                minValue = distances[i]
                minIndex = i
        centroidsDataFrame[minIndex] = centroidsDataFrame[minIndex].append(x)
        del i, minIndex, minValue, distances
    del xi, x
    
    #storing the means of the new centroids means
    newMeans = []
    for i in centroidsDataFrame:
        newMeans.append(round(i.mean(), 3))
    del i
    
    #comparing the new means with the old one to terminate the program if no difference
    flag = True
    for i in range(len(means)):
        for j in Trainingdf.columns:
            if (means[i][j] != newMeans[i][j]):
                flag = False
    del i, j
    
    if(flag == True):
        del flag, newMeans
        break
    else:
        means = newMeans
    del newMeans, flag

#printing the centroids and their dataframes
for i in range(len(centroidsDataFrame)):    
    print("Cluster ", i + 1, ", of Centroid ")
    
    for j in Trainingdf.columns:
        print(j , ":", means[i][j])
    print("\nwith objects: ")
    print(centroidsDataFrame[i])
    print("\n")




