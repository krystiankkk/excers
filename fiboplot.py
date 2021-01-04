import matplotlib.pyplot as plt
tab = []
tab.append(0)
tab.append(1)
tab.append(1)
licz=[]
licz.append(0)
licz.append(1)
licz.append(2)
ff

def fibo(n):

    for i in range(3,n):
        tab.append(tab[i-1]+tab[i-2])
        licz.append(i)
    print(tab)
    print(licz)
    fig, ax = plt.subplots()
    ax.plot(licz, tab,'.')
    ax.set(xlabel='Kolejny wyraz', ylabel='Wartość',
           title='Wykres ciagu Fibo')
    ax.grid()
    fig.savefig("test.png")
    plt.show()


fibo(int(input()))