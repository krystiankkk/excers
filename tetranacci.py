import matplotlib.pyplot as plt

x=[0,1,2,3,4]
val=[0,0,0,1,1]
def tetranacci(n):
    for i in range(5,n):
        val.append(val[i-1]+val[i-2]+val[i-3]+val[i-4])
        x.append(i)
    print(x)
    print(val)
    fig, ax = plt.subplots()
    ax.plot(x,val)
    plt.grid()
    plt.show()
tetranacci(10)