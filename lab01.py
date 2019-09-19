import numpy as np

def linear_regression(x, y, eps=0):
    X=design_matrix(x)
    w = linear(X,y,eps)
    return w

def linear(X,y,eps=0):
    M = np.dot(np.transpose(X), X)+eps*identity(X.shape[0])
    return np.dot(np.linalg.inv(M),np.dot(np.transpose(X),y) )

def design_matrix(x):
    X = np.zeros([len(x),len(x)])
    for i in range(len(x)):
        for p in range(len(x)):
            X[i,p] = x[i]**p
    
    return X

def least_square(y1,y2):
    y=y1-y2
    y=np.square(y)
    return np.mean(y)

def question_4(w):
    order =0;
    for i in range(len(w)-1,-1,-1):
        if ( w[i] !=0 ):
            order = i
    return order



