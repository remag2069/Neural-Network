from suppliments import matrix as m

# inp=[]
# out=[]
# t=[]
# weights=[]
# size_inp=int(input('No. of data sets'))
# size_t=int(input('No. of elements in each data set'))
# for i in range(0,size_inp):
#     t=[]
#     print('set '+str(i)+': ')
#     for j in range(0,size_t):
#         t.append(float(input('x'+str(j)+': ')))
#     t.append(1)
#     inp.append(t)
#     out.append(int(input('expected output:')))


# training_data={'inp':inp,'out':out}

# weights=m.assign_w(size_t,size_t)



# # print(m.activation(m.dot(training_data['inp'][1],weights)[1]))


class nn():
    def __init__(self,layers):
        self.l=len(layers)
        self.weights=[]
        self.learning_rate=.5
        for i in range(self.l-1):
            w=m.assign_w(layers[i+1],layers[i])
            self.weights.append(w)

    def hi(self):
        print(self.l)
        print(self.weights)
        # print(self.weights[2][0][1])
    
    def forward(self,input):
        x=input
        self.a=[]
        for i in range(self.l-1):
            x.append(1)
            self.a.append(x)
            x=(m.activation(m.dot(self.weights[i],x),'sigmoid'))

        self.y_=x
        print(x)


    def bp(self,i,j,k):
        # print('i' +str(i)+'    j '+str(j)+'    k '+str(k)+'::::     ' +str(self.a[i][k]))
        # print(self.weights[i][j][k])
        calc=self.weights[i][j][k]*self.a[i][k]*(1-self.a[i][k])
        print('  1 calc    '+str(self.weights[i][j][k])+'*'+str(self.a[i][k]*(1-self.a[i][k])))

        calc2=0
        if i>self.l-3:
            # print('i'+str(i))
            return calc
        for p in range(len(self.weights[i+1])):
            calc2=calc2+self.bp(i+1,p,j)
        print('   calc    '+str(self.weights[i][j][k])+'*'+str(self.a[i][k]*(1-self.a[i][k]))+'   calc2    '+str(calc2))
        return calc*calc2
    def backward(self,y):
        i=2
        j=0
        k=0
        correction=self.bp(i,j,k)
        # print('      ddddddd                 '+str(correction))
        correction=correction/(self.weights[i][j][k]*(1.0-self.a[i][k]))
        print('      ddddddd                 '+str(correction))
        correction=correction*self.learning_rate*2*(y-self.y_[0])
        self.weights[i][j][k]=self.weights[i][j][k]+correction


    def train(self,x,y):
        for i in range(100):
            for i in range(len(x)):
                self.forward(x[i])
                self.backward(y)

x=[[1,1],[0,0],[1,0],[0,1]]
y=[0,0,1,1]

k=nn([2,2,2,1])
# k.hi()
# for i in range(20):
    print('######################################################################')
    # print(k.weights)
    k.forward([3,6])
    k.backward(1)



# w=m.assign_w(3,2)
# print(w)