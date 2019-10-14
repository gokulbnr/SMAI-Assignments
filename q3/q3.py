import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import sys
from sklearn.metrics import accuracy_score

def file_read(filename):
    X=[]
    f=open(filename,'r')
    for line in f:
        line = line.split(",")
        X.append([float(x) for x in line[:]])
    X = np.asarray(X)
    return X


def get_plot(L,C,trX,trY,teX,teY,k):
    l=LogisticRegression(penalty=L,C=C)
    l.fit(trX,trY)    
    lc=l.coef_.ravel()    
    lp=plt.subplot(1,2,k)
    if k==1:
        lp.set_title("L1 Penalty, C=%.2f"%C)
    else:
        lp.set_title("L2 Penalty, C=%.2f"%C)
    lp.imshow(np.abs(lc.reshape(28,28)),interpolation='nearest',cmap='gray')
    lp.set_xticks(())
    lp.set_yticks(())
    predictions=l.predict(teX)
    return accuracy_score(predictions,teY)


def main(args):
    trX=file_read(args[0])
    trY=file_read(args[1])
    teX=file_read(args[2])
    teY=file_read(args[3])

    for C in [1,0.1,0.001,0.0001,0.00001]:
        print get_plot('l1',C,trX,trY,teX,teY,1)
        print get_plot('l2',C,trX,trY,teX,teY,2)
        plt.show()

main(sys.argv[1:])
