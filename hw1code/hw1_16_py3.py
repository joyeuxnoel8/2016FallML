# This code is for Python 3.x

import numpy as np
import random

# Read files
X = []
with open('hw1_15_train_x.dat','r') as f:
    for line in f:
        X.append(list(map(float,line.split(' '))))     
X = np.matrix(X)


Tar = []
with open('hw1_15_train_y.dat','r') as f:
    for line in f:
        Tar.append(list(map(int,line.split(' '))))
    Tar=np.matrix(Tar)


# Initiallize
Size = len(Tar)
cycle = 2000
updatelist = np.zeros((cycle,1))


# Train
for i in list(range(cycle)):
    W = np.zeros((5,1))
    
    order = random.sample(list(range(Size)),Size)
    indlast = 0
    indnew = 0
    update = 0

    Xn = X[indnew,:]

    Y = -1

    completeness = 0

    while (True):
        
        indnew = (indlast+1)%Size
        
        if ( Y != Tar[order[indlast]] ):
            W = W + np.multiply(Tar[order[indlast]],Xn.T)
            Xn = X[order[indnew],:]
            Y = np.sign(Xn*W)
            if Y == 0:
                Y = -1
            completeness = 0
            update += 1
            
        else:               
            completeness = completeness +1
            Xn = X[order[indnew],:]
            Y = np.sign(Xn*W)
            if Y == 0:
                Y = -1
                
            if completeness == Size :
                #print'update    ',update
                #print'indlast   ',indlast
                break

        indlast = indnew
        
    updatelist[i] = update
    
    if i%100 == 1:
        print('cycle    ',i)
        print('average update   ',np.sum(updatelist)/i)

print('average update   ',np.sum(updatelist)/cycle)

# Test
Y_matrix = np.sign(X*W)
correct = 0
n = 0
for i in np.array(range(Size)) :
    if Y_matrix[i] == Tar[i] :
        correct += 1
    else:
        print('Falied at',n,'th vector')
        print('Failed')
        break
if correct == 400:
    print('Succeed')

# Plot
import matplotlib.pyplot as plt
myhist = np.hstack(updatelist)
plt.hist(myhist, bins='auto')
plt.title("Updates - Frequency Plot")
plt.show()

# average update = 39,40
