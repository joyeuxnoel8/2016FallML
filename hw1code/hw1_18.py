"""
This code is for Python 3.x
Run the pocket algorithm with a total of 50 updates on D, and verify the 
performance of wpocket using the test set. Please repeat your experiment for 
2000 times, each with a different random seed. What is the average error rate 
on the test set? Plot a histogram to show error rate versus frequency
"""

import numpy as np
import random

# Read Training Data
X = []
TargetY = []
with open('hw1_18_train.dat','r') as f:
    for line in f:
        raw = line.split()
        rawx = [1] + raw[:-1]
        X.append(tuple(rawx))
        TargetY.append(int(raw[-1]))
f.closed

X = np.matrix(X)
X = X.astype(np.float)
TargetY = np.array(TargetY)
TargetY.shape = (len(TargetY),1)


# Read Testing Data
Xtest = []
TargetYtest = []
with open('hw1_18_test.dat','r') as f:
    for line in f:
        raw = line.split()
        rawx = [1] + raw[:-1]
        Xtest.append(tuple(rawx))
        TargetYtest.append(int(raw[-1]))
f.closed

Xtest = np.matrix(Xtest)
Xtest = Xtest.astype(np.float)
TargetYtest = np.array(TargetYtest)
TargetYtest.shape = (len(TargetYtest),1)


# Initiallize
Sizetrain = len(TargetY)
Sizetest = len(TargetYtest)
cycle = 1
cycle = 2000
updatelimit = 50
eta = 1
ErrRate = np.zeros((cycle,1))


# Train
for i in list(range(cycle)):
    W = np.zeros((5,1))
    Wpocket = W
    order = random.sample(list(range(Sizetrain)),Sizetrain)
    indlast = 0
    indnew = 0
    update = 0
    wErrSum = Sizetest

    Xn = X[indnew,:]

    Y = -1

    while (update < updatelimit):
        
        indnew = (indlast+1)%Sizetrain
        
        # If update w
        if ( Y != ( TargetY[order[indlast]]>0 ) ):
            W = W + eta * np.multiply(TargetY[order[indlast]],Xn.T)
            Xn = X[order[indnew],:]
            Y = Xn*W > 0
            update += 1
            
            # Check if update pocket w, using testing datasets
            Yarray = Xtest*W > 0
            ErrSum = np.sum( ( TargetYtest>0) != Yarray)
            if ErrSum < wErrSum:
                Wpocket = W
                wErrSum = ErrSum
        else:
            Xn = X[order[indnew],:]
            Y = Xn*W > 0

        indlast = indnew

    ErrRate[i] = wErrSum/Sizetest
    
    if i%100 == 1:
        print('cycle        ',i)
        print('Error Rate   ',ErrRate)

print('Error Rate   ',ErrRate)
print('Average Error Rate   ',np.sum(ErrRate)/cycle)


# Plot
import matplotlib.pyplot as plt
myhist = np.hstack(ErrRate)
plt.hist(myhist, bins='auto', range=(0,1))
plt.title("Error Rate - Frequency Plot")
plt.show()

# Error Rate ~= 0.1 ~ 0.2
# Average Error Rate = 0.127501