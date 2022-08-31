Примери могућих решења
======================

Сваки програмерски задатак можете да решите на мноштво различитих
начина. Обично тражимо оне једноставније, краће, брже или оне који троше
најмање меморије. Овде ћемо дати примере решења за задатке из претходних
лекција која су бирана према методама које сте већ научили. То свакако
нису једина добра решења. Пробајте да решите задатак и на неки други
начин.

Увод у процесирање низова података у Пајтону
--------------------------------------------

**Задатак 1**

.. code:: ipython3

    def najveci_od_tri(A0, A1, A2):
        najveci = A0
        if A1 > najveci: najveci = A1
        if A2 > najveci: najveci = A2
        return najveci

**Задатак 2**

.. code:: ipython3

    def najveci_od_pet(A0, A1, A2, A3, A4):
        najveci = A0
        if A1 > najveci: najveci = A1
        if A2 > najveci: najveci = A2
        if A3 > najveci: najveci = A3
        if A4 > najveci: najveci = A4
        return najveci

**Задатак 3**

.. code:: ipython3

    def max_niza(A):
        najveci = A[0]
        for i in range(len(A)):
            if A[i] > najveci: najveci = A[i]
        return najveci

**Задатак 4**

.. code:: ipython3

    def zbir_najboljih_5(Z1, Z2, Z3, Z4, Z5, Z6):
        L=[Z1, Z2, Z3, Z4, Z5, Z6]
        zbir5=sum(L)-min(L)
        return zbir5

**Задатак 5**

.. code:: ipython3

    def srednji_od_tri(A0, A1, A2):
        L=[A0, A1, A2]
        srednji=sum(L)-max(L)-min(L)
        return srednji

**Задатак 6**

.. code:: ipython3

    def srednja_vrednost_bez_ekstrema(ocene):
        zbe=sum(ocene)-min(ocene)-max(ocene)
        svbe=zbe/(len(ocene)-2)
        return svbe

Сортирање
---------

**Задатак 1**

.. code:: ipython3

    def kti_po_velicini(L, k):
        L.sort(reverse=True)
        return L[k-1]

**Задатак 2**

.. code:: ipython3

    def permutacija_od(L, M):
        ip=L.sort()==M.sort()
        return ip

**Задатак 3**

.. code:: ipython3

    # prvo rešenje (po analigiji sa selection_sort iz lekcije)
    def selection_sort_desc(L):
        n = len(L)
        if n <= 1: return
        for i in range (n-1):
            m = i
            for j in range(i+1,n):
                if L[j] > L[m]:
                    m = j
            L[i], L[m] = L[m], L[i]

.. code:: ipython3

    # drugo rešenje (iskoristimo selection_sort i obrnemo redosled)
    def selection_sort_desc(L):
        L=selection_sort(L)
        return L.reverse()

**Задатак 4**

.. code:: ipython3

    # rešenje po analigiji sa bubble_sort iz lekcije
    def bubble_sort_desc(L):
        n = len(L)
        if n <= 1: return
        zamena = True
        while zamena:
            zamena = False
            for i in range(n-1):
                if L[i] < L[i+1]:
                    zamena = True
                    L[i], L[i+1] = L[i+1], L[i]
            n -= 1

**Задатак 5**

.. code:: ipython3

    def h_indeks(citiranost):
        n=len(citiranost)
        if n>1:
            citiranost.sort(reverse=True)
        h=0
        while citiranost[h]>=h+1:
            h+=1
            if h==n:
                return h
        return h

**Задатак 6**

Решење овог задатка који табелу смешта у листу није једноставно. Боље је
искористити функције за рад са табелама које постоје у библиотеци
*pandas*. Овде ћемо дати примере решења на оба начина. Имајте у виду да
прво решење решење не би радило кад имамо више ученика са истим
презименом. За то бисмо морали да унесемо још неку линију кôда.

.. code:: ipython3

    # rešenje sa standardnom bibliotekom
    def po_prezimenu(razred):
        kolona=[red[1] for red in razred]
        kolona0=kolona.copy()  # čuvamo original kolone
        kolona.sort()
        sortirani_razred=[]
        for s in kolona:
            sortirani_razred.append(razred[kolona0.index(s)])
        return sortirani_razred

.. code:: ipython3

    # rešenje sa pandas bibliotekom
    import pandas as pd
    
    def po_prezimenu(razred):
        df=pd.DataFrame(razred)  # listu pretvaramo u dataframe
        sdf=df.sort_values(1)    # sortiramo po koloni sa indeksom 1
        return sdf

**Задатак 7**

Слично као у претходном задатку, решавање овог задатка само са листама
није једноставно. Зато смо дали пример и са коришћењем *pandas*
библиотеке.

.. code:: ipython3

    # rešenje sa listama
    def rang_lista(T):
        for red in T:
            red.append(sum(red[1:]))
        kolona=[red[-1] for red in T] # uzimamo poslednju kolonu za sortiranje
        kolona0=kolona.copy()
        kolona.sort(reverse=True)
        rl=[]
        for s in kolona:
            rl.append(T[kolona0.index(s)])
        return rl

.. code:: ipython3

    # rešenje sa bibliotekom pandas
    import pandas as pd
    
    def rang_lista(T):
        df=pd.DataFrame(T)
        df['sum']=df.iloc[:,1:].sum(axis=1)
        sdf=df.sort_values('sum',ascending=False)
        return sdf

**Задатак 8**

За овај задатак дајемо два решења. У првом користимо само листе, док у
другом користимо и колекцију типа скуп. Скупови имају својство да су сви
елементи јединствени. Код њих нема понављања. Ако листу претворимо у
скуп, Пајтон ће избрисати све елементе који су дупликати.

.. code:: ipython3

    # prvo rešenje: koristimo samo liste
    def svi_razliciti(L):
        n=len(L)
        for i in range(n):
            if L[i] in L[i+1:]:
                return False
        return True

.. code:: ipython3

    # drugo rešenje: koristimo i skup
    def svi_razliciti(L):
        if len(L)==len(set(L)):
            return True
        else:
            return False

Филтрирање и претраживање
-------------------------

**Задатак 1**

.. code:: ipython3

    morski_plodovi = [
       ["Туна", 116, 0, 26, 1],
       ["Ослић", 88, 0, 17.2, 0.8],
       ["Пастрмка", 119, 0, 18, 5],
       ["Лосос", 116, 0, 20, 3.5],
       ["Скуша", 205, 0, 19, 14],
       ["Сардине", 135, 0, 18, 5],
       ["Харинга", 158, 0, 18, 9],
       ["Бакалар", 82, 0, 18, 0.7],
       ["Сом", 95, 0, 16.4, 2.8],
       ["Шаран", 127, 0, 17.6, 5.6],
       ["Орада", 115, 0, 16.5, 5.5],
       ["Јегуља", 184, 0, 18.4, 11.7],
       ["Шкампи", 106, 1, 20, 2],
       ["Дагње", 86, 4, 12, 2],
       ["Козице", 71, 1, 13, 1],
       ["Лигње", 92, 3, 15.6, 1.3],
       ["Хоботница", 81, 0, 16.4, 0.9],
       ["Јастог", 112, 0, 20, 1.5]]
    
    print([red[0] for red in morski_plodovi if red[2] == 0 and red[4] < 10])


.. parsed-literal::

    ['Туна', 'Ослић', 'Пастрмка', 'Лосос', 'Сардине', 'Харинга', 'Бакалар', 'Сом', 'Шаран', 'Орада', 'Хоботница', 'Јастог']
    

**Задатак 2**

.. code:: ipython3

    takmicari = [["Алексић Алекса", 4.25, 4.31, 4.22],
                 ["Бранковић Бранко", 3.89, 4.02, 4.05],
                 ["Вуковић Вук", 0, 3.91, 4.1],
                 ["Гавриловић Гаврило", 3.78, 3.26, 3.11],
                 ["Дејановић Дејан", 4.56, 4.31, 4.27],
                 ["Ђорђевић Ђорђе", 4.63, 4.6, 4.52],
                 ["Жарковић Жарко", 3.47, 3.51, 3.58],
                 ["Зорић Зоран", 4.12, 4.15, 4.09],
                 ["Ивановић Иван", 3.91, 3.26, 0],
                 ["Јовановић Јован", 4.01, 4.1, 4.12],
                 ["Костић Коста", 3.51, 3.72, 3.41],
                 ["Лукић Лука", 2.15, 2.17, 2.18],
                 ["Марковић Марко", 3.39, 0, 3.26],
                 ["Ненадовић Ненад", 4.25, 4.18, 4.22],
                 ["Огњановић Огњен", 4.31, 4.26, 4.12],
                 ["Петровић Петар", 4.23, 4.34, 4.34],
                 ["Ракић Рака", 3.51, 3.54, 3.62],
                 ["Станојевић Станоје", 4.57, 4.59, 4.63]]
    
    print([red for red in takmicari if 0 in red])


.. parsed-literal::

    [['Вуковић Вук', 0, 3.91, 4.1], ['Ивановић Иван', 3.91, 3.26, 0], ['Марковић Марко', 3.39, 0, 3.26]]
    

**Задатак 3**

.. code:: ipython3

    podaci = [
        ["Петровић",  "Петар", "0308003800019", "м", 8, 4.52],
        ["Јаснић",    "Јасна", "1210003805026", "ж", 8, 5.00],
        ["Аничић",    "Аница", "1105004805019", "ж", 7, 4.11],
        ["Веснић",    "Весна", "2901005705011", "ж", 6, 5.00],
        ["Ђорђевић",  "Ђорђе", "1504005700012", "м", 6, 3.12],
        ["Милошев",   "Милош", "1506004400056", "м", 7, 2.51],
        ["Милошев",   "Петар", "1506004400057", "м", 7, 2.48],
        ["Ненадовић", "Ненад", "2109003800046", "м", 8, 3.58],
        ["Ненадовић", "Јасна", "2109003805021", "ж", 8, 4.21]]
    
    # Направи нову табелу коју чине само ученици осмог разреда.
    print([red for red in podaci if red[4] == 8])
    
    # Направи нову табелу коју чине само врло добри ученици.
    print([red for red in podaci if 3.50 <= red[5] < 4.50])
    
    # Направи нову табелу коју чине само дечаци који нису одлични.
    print([red for red in podaci if red[3] == "м" and red[5] < 4.50])


.. parsed-literal::

    [['Петровић', 'Петар', '0308003800019', 'м', 8, 4.52], ['Јаснић', 'Јасна', '1210003805026', 'ж', 8, 5.0], ['Ненадовић', 'Ненад', '2109003800046', 'м', 8, 3.58], ['Ненадовић', 'Јасна', '2109003805021', 'ж', 8, 4.21]]
    [['Аничић', 'Аница', '1105004805019', 'ж', 7, 4.11], ['Ненадовић', 'Ненад', '2109003800046', 'м', 8, 3.58], ['Ненадовић', 'Јасна', '2109003805021', 'ж', 8, 4.21]]
    [['Ђорђевић', 'Ђорђе', '1504005700012', 'м', 6, 3.12], ['Милошев', 'Милош', '1506004400056', 'м', 7, 2.51], ['Милошев', 'Петар', '1506004400057', 'м', 7, 2.48], ['Ненадовић', 'Ненад', '2109003800046', 'м', 8, 3.58]]
    

**Задатак 4**

.. code:: ipython3

    def nadji_sve(x, L):
        return [i for i in range(len(L)) if L[i] == x]

**Задатак 5**

.. code:: ipython3

    def presek(L, M):
        return [i for i in L if i in M]

**Задатак 6**

.. code:: ipython3

    def razlika(L, M):
        return [i for i in L if i not in M]

**Задатак 7**


**Задатак 8**


**Задатак 9**


Представљање низова података
----------------------------

**Задатак 1**



.. parsed-literal::

    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    

**Задатак 2**


**Задатак 3**


Рад са текстуалним подацима
---------------------------

**Задатак 1**

.. code:: ipython3

    az=""
    for i in range(65,65+26):
        az=az+chr(i)
    print(az)


.. parsed-literal::

    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    

**Задатак 2**

.. code:: ipython3

    def broj_karaktera(L):
        n=0
        for x in L:
            n+=1
        return n

**Задатак 3**

.. code:: ipython3

    def bzi(L):
        n=0
        for x in L:
            if x in ".,:;?!-":
                n+=1
        return n

**Задатак 4**

.. code:: ipython3

    S="String je lista karaktera: slova, cifara i ostalih znakova."
    i=0
    s="ra"
    while s in S[i:]:
        i=S.index(s,i)
        print(i)
        i+=1


.. parsed-literal::

    18
    23
    38
    

**Задатак 5**

.. code:: ipython3

    def jeste_anagram(a,b):    
        a_sms=a.replace(" ","").lower()
        b_sms=b.replace(" ","").lower()
        al=list(a_sms)
        bl=list(b_sms)
        al.sort()
        bl.sort()
        return al==bl


Рад са табелама
---------------

**Задатак 1**



.. parsed-literal::

    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    

**Задатак 2**


**Задатак 3**


Обрада и приказ табеларних података
-----------------------------------

**Задатак 1**

.. code:: ipython3

    bspk=dt.groupby('Continent')
    bspk['Density'].median()


.. parsed-literal::

    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    

**Задатак 2**


**Задатак 3**


Џупитер и Ексел
---------------

**Задатак 1**



.. parsed-literal::

    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    

**Задатак 2**


**Задатак 3**

