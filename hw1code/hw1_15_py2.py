import numpy as np

# read files
X = []
with open('hw1_15_train_x.dat','r') as f:
    for line in f:
        X.append(map(float,line.split(' ')))
X = np.matrix(X)


Tar = []
with open('hw1_15_train_y.dat','r') as f:
    for line in f:
        Tar.append(map(int,line.split(' ')))
    Tar=np.matrix(Tar)


# Initiallize
W = np.zeros((5,1))

Size = len(Tar)

indlast = 0
indnew = 0
update = 0
cycle = 0

Xn = X[indnew,:]

Y = -1

completeness = 0

# Train
while (True):
    
    indnew = (indlast+1)%Size
    
    if (Y != Tar[indlast]):
        W = W + np.multiply(Tar[indlast],Xn.T)
        Xn = X[indnew,:]
        Y = np.sign(Xn*W)
        if Y == 0:
            Y = -1
        completeness = 0
        update += 1
        
    else:               
        completeness = completeness +1
        Xn = X[indnew,:]
        Y = np.sign(Xn*W)
        if Y == 0:
            Y = -1
            
        if completeness == Size :
            print'update    ',update
            print'indlast   ',indlast
            break

    indlast = indnew 

# Test
Y_matrix = np.sign(X*W)
correct = 0
n = 0
for i in xrange(Size) :
    if Y_matrix[i] == Tar[i] :
        correct += 1
    else:
        print 'Falied at',n,'th vector'
        print'Failed'
        break
if correct == 400:
    print'Succeed'

# number of updates = 45
# index of the last updated vector = 135
