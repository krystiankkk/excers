import requests
import matplotlib.pyplot as plt
import numpy
from bs4 import BeautifulSoup
import bubblesort
wyniki=[]
URL = 'https://megalotto.pl/wyniki/lotto/losowania-od-1-Stycznia-1957-do-2-Stycznia-2021'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='list_of_last_drawings_wyniki_lotto')
job_elems = results.find_all('li', class_='numbers_in_list')
#print(results.prettify())
for job_elem in job_elems:
    #print(job_elem.text, end='\n')
    wyniki.append(int(job_elem.text))
bubblesort.bubble(wyniki)
set(wyniki)
list_a=[]
list_b=[]
for wynik in wyniki:
    #print(wynik,wyniki.count(wynik))
    list_a.append(wynik)
    list_b.append(wyniki.count(wynik))
    #list_bs.add(wyniki.count(i))
fig, ax = plt.subplots()
plt.xticks(wyniki,wyniki)
ax.plot(list_a,list_b,marker='o')
ax.grid()
ax.set(xlabel='Liczba',ylabel='Ilość wystąpień')
plt.show()
