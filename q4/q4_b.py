from sklearn.linear_model import Ridge
from sklearn.metrics import accuracy_score
import numpy as np
import sys

def file_read(filename):
    X=[]; Y=[]
    f=open(filename,'r')
    for line in f:
        line = line.split(",")
        Y.append(int(line[len(line)-1]))
        X.append([float(x) for x in line[:len(line)-1]])
    X = np.asarray(X); Y = np.asarray(Y)
    return X, Y

def calculate_accuracy(P,Y):
    return accuracy_score(P,Y)

def binerize(op):
    return np.where(op>0.5,1,0)

def output(X):
    for i in range(X.shape[0]):
        print X[i]

def main(argv):
    trX, trY=file_read(argv[0])
    teX, teY=file_read(argv[1])
    l=Ridge(alpha=0.00000001)
    l.fit(trX,trY)
    trP=l.predict(teX)
    trP=binerize(trP)   
    acc=calculate_accuracy(trP,teY)
    output(trP)

main(sys.argv[1:])
