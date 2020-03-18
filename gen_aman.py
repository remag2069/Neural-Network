#import numpy as np
#import matplotlib.pyplot as plt
import random as r
from suppliments import matrix as s 

#r.seed(123)
inp=[]
out=[]
t=[]
weights=[]
repeat=1000


size_inp=int(input('No. of data sets'))
size_t=int(input('No. of elements in each data set'))
size_o=int(input('No. of output neurons'))


for i in range(0,size_inp):
    t=[]
    print('set '+str(i)+': ')
    for j in range(0,size_t):
        t.append(float(input('x'+str(j)+': ')))
    t.append(1.0)
    inp.append(t)
    t=[]
    for j in range(0,size_o):
        t.append(int(input('expected output y'+str(j)+':')))
    out.append(t)

training_data={'inp':inp,'out':out}

weights=s.assign_w(size_o,size_t)

w_=[]

y_=[]

for i in range(0,size_inp):
    #print(s.dot(weights,training_data['inp']))
    y_=(s.activation(s.dot(weights,training_data['inp'])))
kkk=y_


l=0
for i in range(0,repeat):
    print('y_::'+str(y_))
    e=0
    for j in range(0,size_inp):
        for jk in range(0,size_o):
            #print(y_[j][jk])
            e=e+(training_data['out'][j][jk]-y_[j][jk])**2
    e=e**0.5
    print(e)
    
    t=training_data['out'][l]
    # print(str(t)+'+'+str(l))
    if t==y_[l]:
        pass
    else:
        w_=[]
        #print('in')
        # for k in range(0,size_t+1):
        #     #print(w_)
        #     w_.append(weights[k]+training_data['out'][l]*training_data['inp'][l][k])
        asdfg=s.addmat(1,y_[l],-1,training_data['out'][l])
        w_=s.addmat(1,weights,asdfg,training_data['inp'][l])
        weights=w_    
    print(weights)
    y_=[]
    # for k in range(0,size_inp):
    #     calc=0
    #     for j in range(0,size_t+1):
    #         #print(k)
    #         #print(j)
    #         calc=calc+training_data['inp'][k][j]*weights[j]
    #     if calc>0:
    #         #print('1')
    #         y_.append(1)
    #     else:
    #         #print('-1')
    #         y_.append(-1)
        #print('end')
    for i in range(0,size_inp):
        y_=(s.activation(s.dot(weights,training_data['inp'])))
    if l==size_inp-1:
        l=-1
    l=l+1

print(kkk)

while(True):
    t=[]
    # s=0
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
    # for i in range(0,size_t):
    #     s=s+t[i]*weights[i]
    # if(s>0):
    #     print('GEN_1 predicts the output to be: 1')
    # else:
    #     print('GEN_1 predicts the output to be: -1')
    print(s.activation(s.dot(weights,t)))
