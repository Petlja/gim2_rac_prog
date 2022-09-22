Задаци.
---------

Задатак 1.
''''''''''''''''''''''

Написати Пајтон функцију ``kti_po_velicini(L, k)`` која враћа елемент низа ``L`` који је k-ти по величини
у том низу.

.. activecode:: primer5-Z1
   :runortest: test1, test2, test3
   :nocodelens:

   # -*- acsection: general-init -*-
   # -*- acsection: main -*-

   def kti_po_velicini(L, k):
       # Овде напиши функцију
       return -1234  # поправи овај ред!

   # Провера
   test1 = kti_po_velicini([3, 1, 2, 5, 4, 7, 1, 0], 1)
   test2 = kti_po_velicini([3, 1, 2, 5, 4, 7, 1, 0], 3)
   test3 = kti_po_velicini([3, 1, 2, 5, 4, 7, 1, 0], 8)
   # -*- acsection: after-main -*-
   
   print(test1, test2, test3)
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
           def __kpv(L, k):
              L.sort(reverse=True)
              return L[k-1]
           rez1 = __kpv([3, 1, 2, 5, 4, 7, 1, 0], 1)
           rez2 = __kpv([3, 1, 2, 5, 4, 7, 1, 0], 3)
           rez3 = __kpv([3, 1, 2, 5, 4, 7, 1, 0], 8)
           run_test = acMainSection(test1=test1,test2=test2,test3=test3)
           self.assertEqual(run_test["test1"], rez1, "Вредност променљиве 'test1' треба да буде '%s'" % rez1)
           self.assertEqual(run_test["test2"], rez2, "Вредност променљиве 'test2' треба да буде '%s'" % rez2)
           self.assertEqual(run_test["test3"], rez3, "Вредност променљиве 'test3' треба да буде '%s'" % rez3)
   myTests().main()


Задатак 2*.
''''''''''''''''''''''


За два низа бројева кажемо да је један *пермутација* оног другог ако се елементи првог низа
могу испремештати тако да се добије онај други низ. Написати Пајтон функцију ``permutacija_od(L, M)`` која проверава да ли
је низ ``M`` пермутација низа ``M``.

*Идеја решења.* Сортирај оба низа и провери да ли су добијени низови једнаки!

.. activecode:: primer5-Z5666
   :runortest: test1, test2, test3
   :nocodelens:

   # -*- acsection: general-init -*-
   # -*- acsection: main -*-

   def permutacija_od(L, M):
       # Овде напиши функцију
       return -1234 # поправи овај ред

   test1 = permutacija_od([2, 1, 4, 5, 3], [5, 4, 1, 3, 2]) # jeste
   test2 = permutacija_od([1, 2, 4, 3], [2, 4, 5, 1]) # nije
   test3 = permutacija_od([3, 1, 4, 2], [2, 3, 2, 4]) # nije
   # -*- acsection: after-main -*-

   print(test1, test2, test3)
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
           rez1 = True
           rez2 = False
           rez3 = False
           run_test = acMainSection(test1=test1,test2=test2,test3=test3)
           self.assertEqual(run_test["test1"], rez1, "Вредност променљиве 'test1' треба да буде '%s'" % rez1)
           self.assertEqual(run_test["test2"], rez2, "Вредност променљиве 'test2' треба да буде '%s'" % rez2)
           self.assertEqual(run_test["test3"], rez3, "Вредност променљиве 'test3' треба да буде '%s'" % rez3)
   myTests().main()


Задатак 3.
''''''''''''''''''''''

Написати Пајтон функцију ``selection_sort_desc(L)`` која сортира низ стратегијом бирања највећег елемента
(*selection sort*), тако да елементи низа буду поређани од највећег до најмањег елемента.

.. activecode:: primer5-Z4

   def selection_sort_desc(L):
       # Овде напиши функцију

   # Провера
   test1 = [3, 1, 4, 2, 7]
   selection_sort_desc(test1)
   test2 = [1, 2, 3, 4]
   selection_sort_desc(test2)
   test3 = [4, 3, 2, 1]
   selection_sort_desc(test3)

   print(test1)
   print(test2)
   print(test3)


Задатак 4.
''''''''''''''''''''''

Написати Пајтон функцију ``bubble_sort_desc(L)`` која сортира низ бабл-сорт стратегијом,
али тако да елементи низа буду поређани од највећег до најмањег елемента.

.. activecode:: primer5-Z555

   def bubble_sort_desc(L):
       # Овде напиши функцију

   # Провера
   test1 = [3, 1, 4, 2, 7]
   bubble_sort_desc(test1)
   test2 = [1, 2, 3, 4]
   bubble_sort_desc(test2)
   test3 = [4, 3, 2, 1]
   bubble_sort_desc(test3)
   
   print(test1)
   print(test2)
   print(test3)




Задатак 5*.
''''''''''''''''''''''

*Хиршов h-индекс* је једна од мера научне компетенције истраживача. Хиршов h-индекс неког истраживача је највећи број :math:`n`
такав да тај истраживач има барем :math:`n` научних радова од којих је сваки цитиран барем :math:`n` пута.

На пример,

.. code-block:: text

   Цитираност научних радова     Хиршов h-индекс     Образложење
   -------------------------     ---------------     --------------------------------------------------------
   [0, 0, 0]                     0                   ниједан рад није цитиран ниједном
   [1, 1, 1, 1, 1, 1]            1                   има један рад који је цитиран једном, а нема
                                                     два рада од којих је сваки цитиран бар два птуа
   [1, 2, 1, 1, 1, 1]            1                   (исто као горе)
   [1, 1, 10, 1, 5, 1]           2                   има два рада који су цитирани бар два пута, а нема
                                                     три рада са особином да је сваки цитиран бар три пута
                                                      
Написати Пајтон функцију ``h_indeks(citiranost)`` која за листу са бројевима цитата научних радова истраживача (као у примеру)
рачуна Хиршов h-индекс тог истраживача.

*Идеја решења.* Сортирати листу од већих ка мањим вредностима и онда проверити да ли је на првом месту тако сортиране листе број који
је већи или једнак са 1, да ли је на другом месту број који је већи или једнак са 2, да ли је на трећем месту број који је
већи или једнак са 3 итд. Водити рачуна о томе да индекси низова у Пајтону почињу од 0.

.. activecode:: primer5-Z-хирш
   :runortest: test1, test2, test3, test4
   :nocodelens:

   # -*- acsection: general-init -*-
   # -*- acsection: main -*-

   def h_indeks(citiranost):
       # Овде напиши функцију
       return -1234  # поправи овај ред!

   # Провера
   test1 = h_indeks([0, 0, 0])
   test2 = h_indeks([1, 1, 1, 1, 1, 1])
   test3 = h_indeks([1, 2, 1, 1, 1, 1])
   test4 = h_indeks([1, 1, 10, 1, 5, 1])
   # -*- acsection: after-main -*-
   
   print(test1, test2, test3, test4)
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
           rez1 = 0
           rez2 = 1
           rez3 = 1
           rez4 = 2
           run_test = acMainSection(test1=test1,test2=test2,test3=test3,test4=test4)
           self.assertEqual(run_test["test1"], rez1, "Вредност променљиве 'test1' треба да буде '%s'" % rez1)
           self.assertEqual(run_test["test2"], rez2, "Вредност променљиве 'test2' треба да буде '%s'" % rez2)
           self.assertEqual(run_test["test3"], rez3, "Вредност променљиве 'test3' треба да буде '%s'" % rez3)
           self.assertEqual(run_test["test4"], rez4, "Вредност променљиве 'test4' треба да буде '%s'" % rez4)
   myTests().main()



Задатак 6.
''''''''''''''''''''''

Написати Пајтон функцију ``po_prezimenu(L)`` која податке о ученицима једног разреда сортира по презимену.
Подаци о ученицима су дати низом у коме сваки ред садржи име, презиме и оцене ученика, на пример овако:

.. code-block:: python

   razred = [
       ["Dejan", "Dejanović", 3, 4, 5, 4, 5],
       ["Mara", "Marić", 4, 5, 5, 4, 2],
       ["Miloš", "Milošević", 2, 5, 4, 3, 3],
       ["Petar", "Marković", 5, 4, 5, 5, 5]
   ]

.. activecode:: primer5-Z3
   :includesrc: _src/P05/Po_prezimenu.py

.. infonote::

   Реши задатак и у Пајтон окружењу!
   
   Покрени *IDLE*, из фолдера ``P05`` учитај датотеку ``Po_prezimenu.py`` и ту реши задатак.

Задатак 7.
''''''''''''''''''''''

На такмичењу из информатике такмичари су радили по четири задатка. Подаци о именима такмичара и о томе колико су
поена за који задатак освојили дати су низом као у следећем примеру:

.. code-block:: python

   takmicenje = [
       ["Dejan", 25, 25, 0, 25],
       ["Mira", 25, 0, 20, 25],
       ["Milan", 0, 0, 10, 0],
       ["Milica", 25, 25, 25, 25],
       ["Nenad", 10, 0, 25, 5]
   ]
   
Написати Пајтон функцију ``rang_lista(T)`` која за овако представљене резултате такмичара исписује ранг-листу. На пример,

.. code-block:: python

    rang_lista(takmicenje)

треба да испише:

.. code-block:: text

    Milica 100
    Dejan 75
    Mira 70
    Nenad 40

.. activecode:: primer5-Z7
   :includesrc: _src/P05/Rang_lista.py

.. infonote::

   Реши задатак и у Пајтон окружењу!
   
   Покрени *IDLE*, из фолдера ``P05`` учитај датотеку ``Rang_lista.py`` и ту реши задатак.


Задатак 8.
''''''''''''''''''''''

Написати Пајтон функцију ``svi_razliciti(L)`` која проверава да ли су сви елементи низа ``L`` различити.

.. activecode:: primer5-Z6
   :includesrc: _src/P05/Svi_razliciti.py

.. infonote::

   Реши задатак и у Пајтон окружењу!
   
   Покрени *IDLE*, из фолдера ``P05`` учитај датотеку ``Svi_razliciti.py`` и ту реши задатак.