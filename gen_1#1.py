#import numpy as np
#import matplotlib.pyplot as plt
import random as r
from suppliments import matrix as s 

#r.seed(123)
inp=[]
out=[]
t=[]
weights=[]
repeat=500


size_inp=int(input('No. of data sets'))
size_t=int(input('No. of elements in each data set'))
size_o=int(input('No. of output neurons'))
actfn=input('type of activation function: (\'step\' OR \'sigmoid\')')


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

# for i in range(0,size_inp):
print('inp'+str(training_data['inp']))
y_=(s.activation(s.dot(weights,training_data['inp']),actfn))
kkk=y_

print('#####################################################################################################################################')
print('weights'+str(weights))

for i in range(0,repeat):
    print('y_::'+str(y_))
            # e=0
            # for j in range(0,size_inp):
            #     for jk in range(0,size_o):
            #         #print(y_[j][jk])
            #         e=e+(training_data['out'][j][jk]-y_[j][jk])**2
            # e=e**0.5
            # print(e)
    l=r.randint(0,size_inp-1)
    t=training_data['out'][l]
    print(str(t)+'+'+str(l))
    if t==y_[l]:
        pass
    else:
        w_=[]
        #print('in')
        # for k in range(0,size_t+1):
        #     #print(w_)
        #     w_.append(weights[k]+training_data['out'][l]*training_data['inp'][l][k])
        c2=s.addmat(1,training_data['out'][l],-1,y_[l])
        print('this is th enew delta::::'+str(c2))
        w_=s.addmat(1,weights,c2,training_data['inp'][l])
        weights=w_    
    print('weights:::::'+str(weights))
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
    print("++++++++++++++++++++++++++++++++++++++++++++++")
    # for i in range(0,size_inp):
    y_=(s.activation(s.dot(weights,training_data['inp']),actfn))

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
    print(s.activation(s.dot(weights,t),actfn))
