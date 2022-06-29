#!/usr/bin/env python
# coding: utf-8

# In[4]:


import math
import pandas as pd

GDP_Growth = [2.27, 6.9, 1.71, 2.22, 6.68, 1.79]
Countries = ['United States', 'China', 'Japan', 'Germany', 'India', 'UK']

def getSum(numberlist):
    sum = 0
    for x in numberlist:
        sum = sum + x
        return sum
sum = getSum(GDP_Growth)
n = len(GDP_Growth)

mean = sum/n

def getMean():
    sum = 0
    for x in numberlist:
        sum = sum + x
    n = len(GDP_Growth)
    mean = sum/n
    return mean

print('Sum:', sum)
print('Mean:', mean)


# In[6]:


deltaMean = []

def getMeanDiff(numberlist):
    for i in numberlist:
        difference = i-mean
        deltaMean.append(difference) 
    return difference

deltaMeanSQ = []

def getMeanDiffSQ(numberlistt):
    for difference in deltaMean:
        differenceSQ = difference **2
        deltaMeanSQ.append(differenceSQ)
    return differenceSQ

print("Mean Difference:", getMeanDiff(GDP_Growth))
print("Mean Differnce Squared: ", getMeanDiffSQ(GDP_Growth))
print("Mean Differnces Squared: ", deltaMeanSQ)


# In[8]:


deltaMeanSQ_Sum = getSum(deltaMeanSQ)

def getVariance():
    variance = deltaMeanSQ_Sum/n
    return variance

def getStandardDeviation():
    square = math.sqrt(getVariance())
    return square

print("Variance:", getVariance())
print("Standard Deviation:", getStandardDeviation())

GDP_Growth = [2.27, 6.9, 1.71, 2.22, 6.68, 1.79]
def quickly_calc2(GDP_Growth):
    df = pd.DataFrame(GDP_Growth)
    median = df.median()
    return ('Median GDP Growth {}/n' .format(median[0]))
            
print(quickly_calc2(GDP_Growth))

for Countries, GDP_Growth in zip(Countries, GDP_Growth):
    print(Countries, GDP_Growth)


# In[ ]:




