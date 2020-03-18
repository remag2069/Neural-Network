from suppliments import matrix as m
import matplotlib.pyplot as plt


class nn():
    def __init__(self,layers):
        self.l=len(layers)
        self.weights=[]
        self.learning_rate=0.2
        self.plotloss=[]
        for i in range(self.l-1):
            w=m.assign_w(layers[i+1],layers[i])
            self.weights.append(w)
        f=open('f.txt','w')
        f.write(str(self.weights))
        f.close()

    def hi(self):
        print(self.l)
        print(self.weights)
        # print(self.weights[2][0][1])
    
    def forward(self,input):
        x=[]
        m.equate(x,input)
        # print(input)
        # print(x)
        self.a=[]
        for i in range(self.l-1):
            x.append(1)
            self.a.append(x)
            x=(m.activation(m.dot(self.weights[i],x),'sigmoid'))
        self.a.append(x)
        self.y_=x
        print(x)
        # print(self.a)


    def bp(self,i,j,k):
        # print('i' +str(i)+'    j '+str(j)+'    k '+str(k)+'::::     ' +str(self.a[i+1][j]))
        # print(self.weights[i][j][k])
        calc=self.weights[i][j][k]*self.a[i+1][j]*(1-self.a[i+1][j])
        # print('  1 calc    '+str(self.weights[i][j][k])+'*'+str(self.a[i+1][j]*(1-self.a[i+1][j])))

        calc2=0
        if i>self.l-3:
            # print('i'+str(i))
            return calc
        for p in range(len(self.weights[i+1])):
            calc2=calc2+self.bp(i+1,p,j)
        # print('   calc    '+str(self.weights[i][j][k])+'*'+str(self.a[i+1][j]*(1-self.a[i+1][j]))+'   calc2    '+str(calc2))
        return calc*calc2
    def backward(self,y):
        # i=1
        # j=0
        # k=0
        self.loss=(y-self.y_[0])**2
        # print('loss:::::'+str(self.loss))
        for i in range(len(self.weights)):
            for j in range(len(self.weights[i])):
                for k in range(len(self.weights[i][j])):
                    # print(self.a)
                    correction=self.bp(i,j,k)
                    # print('      ddddddd                 '+str(correction))
                    correction=correction/(self.weights[i][j][k])
                    # print('      ddddddd                 '+str(correction))
                    correction=correction*self.learning_rate*(y-self.y_[0])*(self.a[i][k])
                    self.weights[i][j][k]=self.weights[i][j][k]+correction
                    # print('      ddddddd                 '+str(correction))

    def train(self,x,y):
        self.ploss=0
        f=open('t.txt')
        ch='y'
        self.num=0
        while(ch=='y'):
            self.num=self.num+1
            self.actual_loss=0
            for j in range(len(x)):
                # print(self.weights)
                self.forward(x[j])
                self.backward(y[j])
                self.actual_loss=self.actual_loss+self.loss

                #######################

            if self.num%100==0:
                if int(self.ploss*100)==int(self.actual_loss*100):
                    if self.ploss>self.actual_loss:
                        self.learning_rate=self.learning_rate-0.01
                        print('if if')
                        f=open('t.txt','a')
                        f.write(str(self.num/100)+'if if\n')
                        f.close()
                    else:
                        self.learning_rate=self.learning_rate
                        print(str(self.num/100)+'if else')
                        f=open('t.txt','a')
                        f.write('if else\n')
                        f.close()
                else:
                    f=open('t.txt','a')
                    f.write(str(self.num/100)+'else\n')
                    f.close()
                    print('else')
                    self.ploss=self.actual_loss

                    ###############################
            
            if (self.actual_loss<0.01 or self.num>10000):
                ch='n'
            print('ac_loss   '+str(self.actual_loss))
            self.plotloss.append(self.actual_loss)
            print('num'+str(self.num))
            print('######################################################################')
        f.close()

x=[[1,1],[0,0],[1,0],[0,1]]
y=[0,0,1,1]

k=nn([2,2,1])
# k.hi()
# for i in range(1):
#     print('######################################################################')
#     print(k.weights)
#     k.forward([3,6])
#     k.backward(1)
# k.forward([3,6])


                        # k.train(x,y)
                        # k.forward([1,1])
                        # # print(k.y_)
                        # k.forward([0,0])
                        # # print(k.y_)
                        # k.forward([1,0])
                        # # print(k.y_)
                        # k.forward([0,1])
                        # # print(k.y_)
                        # # print(k.weights)
                        # print('num'+str(k.num))

                        # plt.plot(k.plotloss)
                        # plt.title='1'
                        # plt.show()



# k.learning_rate=2
# k.train(x,y)
# k.forward([1,1])
# # print(k.y_)
# k.forward([0,0])
# # print(k.y_)
# k.forward([1,0])
# # print(k.y_)
# k.forward([0,1])
# # print(k.y_)
# # print(k.weights)
# print('num'+str(k.num))

# plt.plot(k.plotloss)
# plt.title='2'
# plt.show()

# k.learning_rate=15
# k.train(x,y)
# k.forward([1,1])
# # print(k.y_)
# k.forward([0,0])
# # print(k.y_)
# k.forward([1,0])
# # print(k.y_)
# k.forward([0,1])
# # print(k.y_)
# # print(k.weights)
# print('num'+str(k.num))

# plt.plot(k.plotloss)
# plt.title='3'
# plt.show()

# k.learning_rate=0.25
# k.train(x,y)
# k.forward([1,1])
# # print(k.y_)
# k.forward([0,0])
# # print(k.y_)
# k.forward([1,0])
# # print(k.y_)
# k.forward([0,1])
# # print(k.y_)
# # print(k.weights)
# print('num'+str(k.num))

# plt.plot(k.plotloss)
# plt.title='4'
# plt.show()