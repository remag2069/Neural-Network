#import numpy as np
import matplotlib.pyplot as plt
import random as r

#r.seed(123)
inp=[]
out=[]
t=[]
weights=[]
size_inp=int(input('No. of data sets'))
size_t=int(input('No. of elements in each data set'))
for i in range(0,size_inp):
    t=[]
    print('set '+str(i)+': ')
    for j in range(0,size_t):
        t.append(float(input('x'+str(j)+': ')))
    t.append(1)
    inp.append(t)
    out.append(int(input('expected output:')))


training_data={'inp':inp,'out':out}
for i in range(0,size_t):
    weights.append(r.randint(-10,10))
weights.append(5)
w_=[]

y_=[]
print(training_data)
print('hi')
print(weights)

for i in range(0,size_inp):
    calc=0
    for j in range(0,size_t+1):
        calc=calc+training_data['inp'][i][j]*weights[j]
    if calc>0:
        y_.append(1)
    else:
        y_.append(-1)
kkk=y_
for i in range(0,9999):
    print('y_::'+str(y_))
    e=0
    for j in range(0,size_inp):
        e=e+(training_data['out'][j]-y_[j])**2
    e=e**0.5
    print(e)
    l=r.randint(0,size_inp-1)
    t=training_data['out'][l]
    print(str(t)+'+'+str(l))
    if t==y_[l]:
        pass
    else:
        w_=[]
        #print('in')
        for k in range(0,size_t+1):
            #print(w_)
            w_.append(weights[k]+training_data['out'][l]*training_data['inp'][l][k])
        weights=w_    
    print(weights)
    y_=[]
    for k in range(0,size_inp):
        calc=0
        for j in range(0,size_t+1):
            #print(k)
            #print(j)
            calc=calc+training_data['inp'][k][j]*weights[j]
        if calc>0:
            #print('1')
            y_.append(1)
        else:
            #print('-1')
            y_.append(-1)
        #print('end')
print(kkk)

while(True):
    t=[]
    s=0
    kkk=input('woould you like to continue with prediction ? (y/n)')
    if(kkk=='y'):
        pass
    elif (kkk == 'n'):
        break
    else:
        continue
    for i in range(0,size_t):
        t.append(float(input('x'+str(i)+': ')))
    t.append(1)
    for i in range(0,size_t):
        s=s+t[i]*weights[i]
    if(s>0):
        print('GEN_1 predicts the output to be: 1')
    else:
        print('GEN_1 predicts the output to be: -1')



