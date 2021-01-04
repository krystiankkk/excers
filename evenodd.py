odd=[]
even=[]
even_ct=0
odd_ct=0
for i in range(1,21):
    if i != 0:
        if i % 2 == 0:
            even.append(i)
            even_ct+=1
        else:
            odd.append(i)
            odd_ct+=1
print('even numbers: ', even, 'łącznie jest ich:', odd_ct)
print('odd numbers: ', odd, 'łącznie jest ich: ', even_ct)