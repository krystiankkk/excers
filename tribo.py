import matplotlib.pyplot as plt
x = [0, 1, 2, 3]
val = []
val.append(0)
val.append(0)
val.append(1)
val.append(1)

print(val[3])


def tribo(n):
    for i in range(4, n):
        print(i)
        val.append(val[i - 1] + val[i - 2] + val[i - 3])
        x.append(i)
    print(x)
    print(val)
    fig, ax = plt.subplots()
    ax.plot(x,val)
    ax.grid()
    ax.set(xlabel='Wyraz ciagu',ylabel='wartosc')
    plt.show()


tribo(int(input()))
