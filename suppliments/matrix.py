import random as ran
import math as m

# a=[[1,2],[3,4]]
# b=[[4,5],[6,7],[1,2]]

def dot(w,x):
    d=[]
    r=[]
    try:
        for i in range(0,len(x)):
            d=[]
            for k in range(0,len(w)):
                c=0
                for j in range(0,len(x[0])):
                    c=c+x[i][j]*w[k][j]
                d.append(c)
            r.append(d)
    except:
        # print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        # print(x)
        for i in range(0,len(w)):
            c=0
            for j in range(0,len(w[0])):
                # print(j)
                c=c+w[i][j]*x[j]
            r.append(c)

    
    return r

def assign_w(r,c):
    w=[]
    for i in range(0,r):
        t=[]
        for j in range(0,c):
            some=float(ran.randint(-10,10))
            if some==0:
                some=1
            t.append(some)

        t.append(0.5)
        w.append(t)
    return w

def addmat(c1,a,c2,b):
    c=[]
    t=[]
    # print('hhhhhhhhhhhhhh')
    # print(c2)
    # print(b)
    # if len(a)==len(b):
    #     pass
    # else:
    #     print('not compatible addition')
    #     return
    # for i in range(0,len(a)):
    #     t=[]
    #     for j in range(0,len(a[0])):
    #         t.append(c1*a[i][j]+c2*b[i][j])
    #     c.append(t)
    #print(c)
    try:
        for i in range(0,len(a)):
            # print(c2)
            # print(b[i])
            t=[]
            for j in range(0,len(b)):
                t.append(a[i][j]+c2[i]*b[j])
            c.append(t)
    except:
        # for i in range(0,len(a)):
        #     # print(c2)
        #     # print(b[i])
        t=[]
        for j in range(0,len(b)):
            # print(a[i])
            # print(c2)
            t.append(a[j]+c2*b[j])
        # print('c::::::'+str(t))
        c=t

    return c
# addmat(a,b)

def activation(x,s):
    # print(x)
    t=[]
    r=[]
    if(s=='step'):
        try:
            for i in range(0,len(x)):
                t=[]
                for j in range(0,len(x[0])):
                    if x[i][j]>0:
                        t.append(1)
                    else:
                        t.append(0)
                r.append(t)
                #print(r)
        except:
            # print(x)
            for i in range(0,len(x)):
                if x[i]>0:
                    r.append(1)
                else:
                    r.append(0)

    elif(s=='sigmoid'):
        try:
            # print('try')
            for i in range(0,len(x)):
                t=[]
                for j in range(0,len(x[0])):
                    # print('inside sig::::'+str(x[i][j]))
                    if (x[i][j]<-100):
                        t.append(0)
                    else:
                        val=1.0/(1.0+m.exp(-1*x[i][j]))
                        # print('val:::::;'+str(val))
                        if(val<0):
                            t.append(0)
                        elif(val>1):
                            t.append(1)
                        else:
                            t.append(val)
                r.append(t)
                #print(r)
        except:
            # print(x)
            for i in range(0,len(x)):
                if (x[i]<-100):
                        r.append(0)
                else:
                    val=1.0/(1.0+m.exp(-1*x[i]))
                    # print('val:::::;'+str(val))
                    if(val<0):
                        r.append(0)
                    elif(val>1):
                        r.append(1)
                    else:
                        r.append(val)
    return r


def equate(x,y):
    try:
        for i in y:
            x.append(i)
    except:
        x=y

# w=assign_w(3,2)
# print(w)

# dot(a,b)
# print(d)