import matplotlib.pyplot as plt

x=[[1,2],[2,3],[3,4]]
y=[13,45,34]
def graph(x,y):
    for i in range(0,len(x)):
        plt.scatter(x[i][0],x[i][1],y[i],c='g')
    plt.show()

graph(x,y)