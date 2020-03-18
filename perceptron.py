import numpy as np
import matplotlib.pyplot as plt
import random as r

#r.seed(123)
training_data={'inp':[[1,1,1],[0,1,1],[1,0,1],[0,0,1]],'out':[1,1,0,0]}
w1= r.randint(-10,10)
w2= r.randint(-10,10)
weights=[w1,w2,1]
w_=[]
y_=[]
print(training_data)
print('hi')
print(weights)

for i in range(0,4):
    calc=0
    for j in range(0,3):
        calc=calc+training_data['inp'][i][j]*weights[j]
    if calc>0:
        y_.append(1)
    else:
        y_.append(-1)

for i in range(0,10000):
    print('y_::'+str(y_))
    e=0
    for j in range(0,4):
        e=e+(training_data['out'][j]-y_[j])**2
    e=e**0.5
    print(e)
    j=r.randint(0,3)
    t=training_data['out'][j]
    print(str(t)+'+'+str(j))
    if t==y_[j]:
        pass
    else:
        w_=[]
        for k in range(0,3):
            w_.append(weights[k]+training_data['out'][j]*training_data['inp'][j][k])
    weights=w_
    print(weights)
    y_=[]
    for k in range(0,4):
        calc=0
        for j in range(0,3):
            calc=calc+training_data['inp'][k][j]*weights[j]
        if calc>0:
            #print('1')
            y_.append(1)
        else:
            #print('-1')
            y_.append(-1)
        #print('end')