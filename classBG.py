import random
import bubblesort

class biggame():
    def __init__(self, count, lim):
        results = []
        user=[]
        trafione=0
        self.lim = lim
        self.count=count
        results = random.sample(range(1, lim), count)
        #print(bubblesort.bubble(results))
        a=bubblesort.bubble(results)
        for i in range(count):
            print('Podaj',i+1,' liczbę')
            user.append(int(input()))
        bubblesort.bubble(user)
        print('Wyniki losowania: ',results)
        print(user)
        for j in results:
            if j in user:
                trafione += 1
        print(trafione)
        return a

biggame(6,49)
