import bubblesort
import random

res = []
print('Ilość liczb do wylosowania :')
count = int(input())
print('Przedział liczb: ')

ranmin = int(input())
ranmax = int(input())
user = []
trafione=0
res = random.sample(range(ranmin, ranmax), count)
print('Twoje liczby:')
for i in range(count):
    user.append(int(input()))

bubblesort.bubble(res)
bubblesort.bubble(user)
for j in res:
    if j in user:
        trafione+=1
print('Trafiłeś: ',trafione)