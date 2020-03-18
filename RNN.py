import backup as bk
import matplotlib.pyplot as plt
import random as r



def generate():
    x=[]
    y=[]

    for i in range(10):
        k=r.randint(-10,10)
        x.append([int(k),int(k*k+9)])
        y.append(1)
    for i in range(10):
        k=r.randint(-10,10)
        x.append([int(k),int(k*k-7)])
        y.append(0)
    return x,y

# x=[[0.2,0],[4,0],[9,0],[16,0],[-4,0],[-3,0],[-9,0],[-0.2,0]]
# y=[1,1,1,1,0,0,0,0]

x,y=generate()
# for i in range(len(x)):
#     print(str(x[i])+"      :"+str(y[i]))
while True:
    net=bk.nn([2,2,2,1])
    net.train(x,y)
    plt.plot(net.plotloss)
    plt.show()
net.forward([5,19])

